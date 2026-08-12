#!/usr/bin/env python3
"""Archive the current public GlassesResearch site into the Wayback Machine.

Discovery order:
1. Read sitemap.xml if present.
2. Crawl same-origin HTML links from the homepage as a fallback/supplement.
3. Submit each discovered public page individually to Save Page Now.

This intentionally archives pages, not arbitrary external links.
"""

from __future__ import annotations

import argparse
import html.parser
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import deque

USER_AGENT = "GlassesResearch-waybackglasses/1.0 (+https://glassesresearch.org/)"
SKIP_SUFFIXES = (
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".ico", ".pdf", ".zip",
    ".mp4", ".webm", ".css", ".js", ".json", ".xml", ".txt", ".woff", ".woff2",
)


class LinkParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs):
        if tag.lower() != "a":
            return
        for key, value in attrs:
            if key.lower() == "href" and value:
                self.links.append(value)


def fetch(url: str, timeout: int = 30) -> tuple[bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read(), resp.headers.get("Content-Type", "")


def normalize(url: str, base: str, origin: tuple[str, str]) -> str | None:
    joined = urllib.parse.urljoin(base, url)
    parsed = urllib.parse.urlparse(joined)
    if parsed.scheme not in ("http", "https"):
        return None
    if (parsed.scheme, parsed.netloc) != origin:
        return None
    path = parsed.path or "/"
    if path.lower().endswith(SKIP_SUFFIXES):
        return None
    # Strip fragments and tracking/query variants; the public page itself is the preservation target.
    return urllib.parse.urlunparse((parsed.scheme, parsed.netloc, path, "", "", ""))


def sitemap_urls(root: str) -> set[str]:
    result: set[str] = set()
    sitemap = urllib.parse.urljoin(root, "/sitemap.xml")
    try:
        body, _ = fetch(sitemap)
        tree = ET.fromstring(body)
        for elem in tree.iter():
            if elem.tag.endswith("loc") and elem.text:
                result.add(elem.text.strip())
    except Exception as exc:
        print(f"Sitemap unavailable: {exc}", file=sys.stderr)
    return result


def crawl(root: str, max_pages: int) -> set[str]:
    parsed_root = urllib.parse.urlparse(root)
    origin = (parsed_root.scheme, parsed_root.netloc)
    start = urllib.parse.urlunparse((parsed_root.scheme, parsed_root.netloc, parsed_root.path or "/", "", "", ""))
    seen: set[str] = set()
    queue = deque([start])

    while queue and len(seen) < max_pages:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)
        try:
            body, ctype = fetch(url)
        except Exception as exc:
            print(f"DISCOVERY FAIL {url}: {exc}", file=sys.stderr)
            continue
        if "text/html" not in ctype.lower():
            continue
        parser = LinkParser()
        try:
            parser.feed(body.decode("utf-8", errors="ignore"))
        except Exception:
            continue
        for href in parser.links:
            candidate = normalize(href, url, origin)
            if candidate and candidate not in seen:
                queue.append(candidate)
    return seen


def save_page(url: str, timeout: int = 90) -> tuple[bool, str]:
    endpoint = "https://web.archive.org/save/" + url
    req = urllib.request.Request(endpoint, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            final = resp.geturl()
            return 200 <= resp.status < 400, final
    except urllib.error.HTTPError as exc:
        # 302/3xx normally follows automatically; 429 is a rate-limit signal.
        return False, f"HTTP {exc.code}"
    except Exception as exc:
        return False, str(exc)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="https://glassesresearch.org/")
    ap.add_argument("--max-pages", type=int, default=500)
    ap.add_argument("--delay", type=float, default=2.5)
    args = ap.parse_args()

    root = args.root.rstrip("/") + "/"
    urls = sitemap_urls(root)
    crawled = crawl(root, args.max_pages)
    urls.update(crawled)

    parsed_root = urllib.parse.urlparse(root)
    origin = (parsed_root.scheme, parsed_root.netloc)
    clean: set[str] = set()
    for url in urls:
        candidate = normalize(url, root, origin)
        if candidate:
            clean.add(candidate)
    clean.add(root)

    ordered = sorted(clean)
    print(f"Discovered {len(ordered)} public pages for Wayback submission.")

    failures: list[tuple[str, str]] = []
    for idx, url in enumerate(ordered, 1):
        ok, result = save_page(url)
        status = "SAVED" if ok else "FAILED"
        print(f"[{idx}/{len(ordered)}] {status} {url} -> {result}")
        if not ok:
            failures.append((url, result))
        if idx != len(ordered):
            time.sleep(args.delay)

    print(f"Completed: {len(ordered) - len(failures)} saved/submitted, {len(failures)} failed.")
    if failures:
        print("Failures:", file=sys.stderr)
        for url, reason in failures:
            print(f"- {url}: {reason}", file=sys.stderr)
        # Preserve partial success while making the workflow visibly non-clean.
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
