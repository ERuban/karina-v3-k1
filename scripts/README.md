# Website

Source of <https://autumn1rain.github.io/karina-v3-k1/>. The generated pages live in
[`../docs`](../docs) and are published by GitHub Pages.

## Turning the site on (once)

1. **Settings** → **Pages**
2. **Source**: Deploy from a branch
3. **Branch**: `main`, folder **`/docs`** → **Save**

A minute later the site is live. Every later push to `main` republishes it automatically.

## Editing the texts

Never edit the HTML in `docs/` by hand — it is generated and will be overwritten.

- English text lives in the `STRINGS` dict in [`build_site.py`](build_site.py).
- Translations live in `../site-i18n/<lang>.json` with the same keys. A missing key falls
  back to English, so an unfinished translation still builds.
- Styling is the `CSS` string in the same script.

After any change, rebuild and commit the result:

```sh
python3 scripts/build_site.py
```

The script writes `docs/index.html`, the four language folders, `sitemap.xml` and
`robots.txt`, and prints the search-engine title and description length of every page — keep
titles under 60 characters and descriptions under 155.

## Checking before you push

```sh
python3 -m http.server 8000 --directory docs
```

Then open <http://localhost:8000/> and check the pages, including the language switcher at
the bottom.

## Languages

English (source), Russian, Spanish, German, Chinese. To add one: add its code, name and
folder to `LANGS` in the script, drop a `site-i18n/<code>.json` next to the others, rebuild.

Screen strings, menu items and key names stay in English on every page — the firmware's
interface is English, and a reader must be able to match the word to the display.

## Images

`docs/assets/radio-k1.png` and `docs/assets/spectrum.png` come from the manuals in this
repository.
