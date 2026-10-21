#!/usr/bin/env python3
"""Check completeness and safety of public EYLab interface translations.

Only public text is read. No access to private repositories, APIs, or secrets.
"""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ROOT / "translations"
LANGS = ("ru", "en", "zh-CN", "tr")
PLACEHOLDER = re.compile(r"\\{[A-Za-z][A-Za-z0-9_]*\\}")
errors = []

try:
    data = {}
    for lang in LANGS:
        path = LOCALES / f"{lang}.json"
        with path.open(encoding="utf-8") as handle:
            value = json.load(handle)
        if not isinstance(value, dict):
            raise ValueError(f"{path} is not a JSON object")
        if not all(isinstance(k, str) and isinstance(v, str) and v.strip() for k, v in value.items()):
            errors.append(f"{lang}: all keys and translations must be non-empty strings")
        data[lang] = value
except (OSError, json.JSONDecodeError, ValueError) as exc:
    sys.exit(f"Translation files invalid: {exc}")

reference = data["ru"]
for lang, translations in data.items():
    missing = sorted(set(reference) - set(translations))
    extra = sorted(set(translations) - set(reference))
    if missing:
        errors.append(f"{lang}: missing keys: {', '.join(missing)}")
    if extra:
        errors.append(f"{lang}: unknown keys: {', '.join(extra)}")
    for key, localized in translations.items():
        if key not in reference:
            continue
        expected = sorted(PLACEHOLDER.findall(reference[key]))
        actual = sorted(PLACEHOLDER.findall(localized))
        if actual != expected:
            errors.append(f"{lang}.{key}: placeholder mismatch {actual} vs {expected}")

if errors:
    for item in errors:
        print("ERROR:", item)
    sys.exit(1)

print(f"OK: {len(reference)} public UI strings in all {len(LANGS)} locales.")
