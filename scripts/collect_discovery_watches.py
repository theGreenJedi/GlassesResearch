#!/usr/bin/env python3
"""Retain and probe high-value discovery sources after first human/machine discovery.

Watch membership is not evidence verification. A configured URL is preserved even if
robots, authentication, or transient network failures prevent fetching it.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import html
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "research" / "discovery-sources.json"
OUTDIR = ROOT / "research" / "discovery-candidates"
UA = "GlassesResearch-DiscoveryWatch/1.0 (+https://glassesresearch.org/)"


def clean(value: str) -> str:
    value = re.sub(r"<script\b[^>]*>.*?</script>", " ", value, flags=re.I | re.S)
    value = re.sub(r"<style\b[^>]*>.*?</style>", " ", value, flags=re.I | re.S)
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def normalize_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), parsed.path.rstrip("/"), "", ""))


def item_id(url: str, channel: str) -> str:
    return hashlib.sha256(f"watch\n{channel}\n{normalize_url(url)}".encode()).hexdigest()[:16]


def probe(url: str) -> tuple[str, str, str | None]:
    try:
        request = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*;q=0.5"})
        with urllib.request.urlopen(request, timeout=20) as response:
            raw = response.read().decode("utf-8", "ignore")
        match = re.search(r"<title[^>]*>(.*?)</title>", raw, re.I | re.S)
        title = clean(match.group(1)) if match else urllib.parse.urlsplit(url).netloc
        return title, clean(raw)[:1200], None
    except Exception as exc:
        return urllib.parse.urlsplit(url).netloc or url, "Configured durable discovery watch; fetch unavailable during this run.", str(exc)[:300]


def main() -> int:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    watch_sets = {
        "manufacturer_watch": cfg.get("manufacturer_watch_pages", []),
        "research_watch": cfg.get("research_watch_pages", []),
        "community_watch": cfg.get("community_watch_pages", []),
        "retail_watch": cfg.get("retail_watch_pages", []),
    }
    now = dt.datetime.now(dt.timezone.utc)
    day = now.date().isoformat()
    candidates: list[dict] = []
    errors: list[dict] = []
    for channel, urls in watch_sets.items():
        for url in urls:
            title, summary, error = probe(url)
            candidates.append({
                "id": item_id(url, channel),
                "title": f"Durable {channel.replace('_', ' ')}: {title}",
                "url": url,
                "summary": summary,
                "discovery_channel": channel,
                "source": "configured durable watch",
                "scope_lane": "research_radar" if channel == "research_watch" else "core_glasses",
                "status": "candidate",
                "publication_eligible": False,
                "publication_gate_reason": "watch retention is not verification or publication",
                "disposition": "watch",
            })
            if error:
                errors.append({"channel": channel, "url": url, "error": error})

    OUTDIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema": 1,
        "discovered_utc": now.isoformat(),
        "candidate_count": len(candidates),
        "collector_errors": errors,
        "candidates": candidates,
    }
    (OUTDIR / f"watch-{day}.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        f"# Durable discovery watches — {day}", "",
        f"Retained **{len(candidates)}** known high-value source watches.", "",
        "A watch is not verification and does not authorize publication.", "",
    ]
    for item in candidates:
        lines += [f"- [{item['title']}]({item['url']}) — {item['discovery_channel']}"]
    if errors:
        lines += ["", "## Probe warnings", ""] + [f"- {e['url']}: {e['error']}" for e in errors]
    (OUTDIR / f"watch-{day}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Retained {len(candidates)} durable watches; {len(errors)} probe warnings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
