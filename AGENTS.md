# Notes for AI agents working in this repository

This repository holds the Karina (*autumn rain*) firmware for the Quansheng UV-K5 (V3),
UV-K1 and UV-K1(8): release binaries, the author's PDF documentation, and the website
published from `docs/`.

Read this before touching documentation or the site.

## Ground rules

- **The radio's interface is English and stays English.** In every language of every
  document, menu items, on-screen strings, key names (`PTT`, `EXIT`, `MENU`, `VFO`, `SCAN`,
  `SList`, `ATT1`, `NONE`…), program names, file names and URLs are copied verbatim. The
  reader must be able to match the word on the page to the word on the display. Cyrillic
  look-alikes are a bug: `АТТ2` → `ATT2`, `М` → `M`.
- **The author's Russian PDFs are the source of truth.** Everything else is derived from
  them. Do not invent features, values or steps, and never drop a safety warning — these
  documents can brick hardware.
- **Do not edit anything in `docs/`.** It is generated and will be overwritten.

## Layout

| Path | What it is |
| --- | --- |
| `karina-v3-k1-install.pdf`, `karina-v3-k1-manual.pdf` | the author's originals (Russian) |
| `karina-v3-k1-install-en.pdf`, `karina-v3-k1-manual-en.pdf` | English versions of the same |
| `site-docs/<lang>/install.md`, `manual.md` | the documents as website sources |
| `scripts/build_site.py` | the site generator: all page texts and all CSS |
| `docs/` | generated site, published by GitHub Pages |
| `README.md`, `README_RU.md`, `README_ES.md`, `README_DE.md`, `README_ZH.md` | repository front page |

## Rebuilding the site

```sh
python3 scripts/build_site.py
```

Standard library only — no dependencies to install. It writes the five language pages, a
document page per language per document, `sitemap.xml` and `robots.txt`, and prints the
search-engine title/description length of every page (keep titles under 60 characters and
descriptions under 155) plus the section and warning count of every document.

Short page texts live in the `TEXTS` dict at the top of the script, one block per language;
a key a translation omits falls back to English. Styling is the `CSS` string in the same
file.

## Regenerating a document (installation guide or manual)

The pipeline that produced `site-docs/` from the PDFs, in case a new PDF revision arrives:

1. **Extract.** Convert the PDF to one Markdown file per page plus its images. Merge
   consecutive text spans that share a style *before* applying `**` / `*` markers, or
   separators between adjacent runs are lost; Word exports frequently position words instead
   of writing a space, so insert a space where the horizontal gap exceeds ~0.22 × font size.
   Drop running headers, footers and bare page numbers by detecting blocks that repeat on
   many pages. Emphasis maps to `**bold**`, `*italic*` and `==highlight==` (the author uses a
   yellow background to mark what is new in a release).
2. **Translate page by page**, in parallel if you like, with the ground rules above. Every
   `![screenshot](images/pXX_Y.png)` line is copied verbatim, in place: the count and order
   must match the source page exactly. Rebuild tables that the extractor flattened into one
   value per line.
3. **Verify mechanically**, not by eye: same screenshot lines per page, no Cyrillic left in a
   non-Russian output, same heading count, protected terms still present. Grep for the
   protected terms yourself instead of trusting a report.
4. **Assemble** the pages into `site-docs/<lang>/<doc>.md`, and put the images into
   `docs/assets/docs/<doc>/`.
5. **Rebuild** and check the result in a browser.

## How a document page is rendered

`render_markdown()` in the generator understands the subset these documents use: `##`–`####`
headings, paragraphs, `-` and numbered lists, tables, images, links, `**bold**`, `*italic*`,
`` `code` `` and `==highlight==`. Every `##` becomes a numbered section id (`s1`, `s2`, …)
used by the sticky table of contents, so section links stay valid in every language.

**Safety notes are rendered large and red.** A paragraph or list item is promoted to a
`.danger` block when it contains `!!!` or opens with a warning word (`ВНИМАНИЕ`, `ВАЖНО`,
`СОХРАНИТЕ`, `ATTENTION`, `WARNING`, `IMPORTANT`, `ACHTUNG`, `ATENCIÓN`, `注意`…). Keep those
markers when editing: dropping an exclamation mark silently downgrades a warning about
backing up the calibration into ordinary text.

## Adding a language

Add its code, name and folder to `LANGS`, add a block with the same keys to `TEXTS`, add
`README_<CODE>.md` with a switcher listing only the *other* languages, and put
`site-docs/<code>/install.md` and `manual.md` in place. Rebuild.
