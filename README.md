# EYLab public interface translations

**Only public interface text, terminology and a safe validation workflow.**
No calculation engines, hidden interpretations, APIs, private source code,
credentials, customer data, or design assets are stored here.

Languages: `ru`, `en`, `zh-CN`, `tr`.

## Using the translations

Load `translations/<language>.json` from the *public* website's front end.
The calculator's internal source and computation engines stay private.
Language-specific SEO pages, canonical URLs, and `hreflang` must be
configured in the website repository separately, not here.

## Automated checks

`.github/workflows/check-translations.yml` validates the translation files
on push, PR, manual run and weekly. It checks that every language has the same
keys, nonempty values and matching template placeholders.

**It does not generate new translations automatically**: that requires a
translation model/service or manually translated strings. The initial
translations were prepared separately; new or changed text requires
editorial review of domain terminology before publishing.

Run locally: `python3 scripts/validate_translations.py`.

## Licensing

Original copyright-protected materials: All rights reserved. See
`LICENSE.txt`. Repository is public/source-visible, but not open source.
Some short labels and generic terms may not be copyright-protected.

## Publishing restrictions

Do not mirror or fetch private GitHub repositories from Actions.
Do not set private repository tokens, credentials or translation API keys.
Do not upload EYLab's calculator HTML/JS, proprietary algorithms,
paid interpretations or databases to this repository.
