#!/usr/bin/env python3
import csv
import os
import subprocess
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

SITEMAP = os.environ.get("SITEMAP_URL", "https://glassesresearch.org/sitemap.xml")
DELAY = float(os.environ.get("WAYBACK_DELAY_SECONDS", "12"))
RETRIES = int(os.environ.get("WAYBACK_RETRIES", "3"))
OUT = os.environ.get("WAYBACK_RESULTS", "wayback-results.csv")
USER_AGENT = "GlassesResearch-Archiver/1.0 (+https://glassesresearch.org/)"


def fetch_xml(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as response:
        return response.read()


def sitemap_urls(url):
    root = ET.fromstring(fetch_xml(url))
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    tag = root.tag.rsplit("}", 1)[-1]
    if tag == "sitemapindex":
        urls = []
        for loc in root.findall("sm:sitemap/sm:loc", ns):
            urls.extend(sitemap_urls(loc.text.strip()))
        return urls
    if tag == "urlset":
        return [loc.text.strip() for loc in root.findall("sm:url/sm:loc", ns) if loc.text]
    raise RuntimeError(f"Unsupported sitemap root: {root.tag}")


def save_url(url):
    endpoint = "https://web.archive.org/save/" + url
    cmd = [
        "curl", "--location", "--silent", "--show-error",
        "--max-time", "120", "--connect-timeout", "30",
        "--user-agent", USER_AGENT,
        "--output", "/dev/null",
        "--write-out", "%{http_code}\t%{url_effective}",
        endpoint,
    ]
    last = ("000", endpoint, "")
    for attempt in range(1, RETRIES + 1):
        p = subprocess.run(cmd, text=True, capture_output=True)
        parts = p.stdout.strip().split("\t", 1)
        status = parts[0] if parts and parts[0] else "000"
        effective = parts[1] if len(parts) > 1 else endpoint
        error = p.stderr.strip()
        last = (status, effective, error)
        try:
            code = int(status)
        except ValueError:
            code = 0
        if p.returncode == 0 and 200 <= code < 400:
            return True, status, effective, error, attempt
        if code == 429 or 500 <= code < 600 or p.returncode != 0:
            time.sleep(20 * attempt)
            continue
        break
    return False, *last, RETRIES


def main():
    urls = list(dict.fromkeys(sitemap_urls(SITEMAP)))
    if "https://glassesresearch.org/" not in urls:
        urls.insert(0, "https://glassesresearch.org/")
    print(f"Wayback archival: {len(urls)} canonical URLs from {SITEMAP}", flush=True)
    successes = failures = 0
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["timestamp_utc", "success", "http_status", "attempts", "url", "wayback_response", "error"])
        for i, url in enumerate(urls, 1):
            ok, status, effective, error, attempts = save_url(url)
            successes += int(ok)
            failures += int(not ok)
            ts = datetime.now(timezone.utc).isoformat()
            w.writerow([ts, "yes" if ok else "no", status, attempts, url, effective, error])
            f.flush()
            print(f"[{i}/{len(urls)}] {'OK' if ok else 'FAIL'} {status} {url}", flush=True)
            if i < len(urls):
                time.sleep(DELAY)
    print(f"Completed: {successes} successful, {failures} failed", flush=True)
    return 0 if failures == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
