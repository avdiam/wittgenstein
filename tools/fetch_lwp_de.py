#!/usr/bin/env python3
"""Fetch the German text of the 526 propositions of the Tractatus from the
Ludwig Wittgenstein Project and write tools/tractatus/tlp_de.json.

The LWP keeps one wiki template per proposition
(Template:Individual-TLP-paragraph-de-N); the file holds their wikitext as it
is, keyed by proposition number. tools/build_html.py reads it to check the
German of the quote cards. The text reproduces the edition of 1922 and is in
the public domain; see LICENSE, section 3.

Not part of build_all.py: run it only to refresh the copy, then rebuild and
read the diff.

Usage:
    python tools/fetch_lwp_de.py
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parent / "tractatus"
API = "https://www.wittgensteinproject.org/w/api.php"
PREFIX = "Template:Individual-TLP-paragraph-de-"


def main():
    nums = json.loads((ASSETS_DIR / "proposition_numbers.json").read_text(encoding="utf8"))
    fetched = {}
    for i in range(0, len(nums), 40):
        titles = "|".join(PREFIX + n for n in nums[i:i + 40])
        url = API + "?" + urllib.parse.urlencode({
            "action": "query", "prop": "revisions", "rvprop": "content",
            "rvslots": "main", "format": "json", "titles": titles,
        })
        req = urllib.request.Request(url, headers={"User-Agent": "study-script/1.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.load(resp)
        for page in data["query"]["pages"].values():
            if "revisions" in page:
                num = page["title"].rsplit("-", 1)[1]
                fetched[num] = page["revisions"][0]["slots"]["main"]["*"]
        time.sleep(1)
    missing = [n for n in nums if n not in fetched]
    if missing:
        sys.exit(f"fetch_lwp_de: not fetched, file left as it was: {missing}")
    ordered = {n: fetched[n] for n in nums}
    with open(ASSETS_DIR / "tlp_de.json", "w", encoding="utf8", newline="\n") as f:
        json.dump(ordered, f, ensure_ascii=False, indent=0)
    print(f"wrote tools/tractatus/tlp_de.json ({len(ordered)} propositions)")


if __name__ == "__main__":
    main()
