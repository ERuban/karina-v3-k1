"""Build the Karina firmware website into docs/ (GitHub Pages).

Usage: python3 scripts/build_site.py

English is the source language and lives in STRINGS below. Translations are optional
JSON files in site-i18n/<lang>.json holding the same keys; missing keys fall back to
English, so a half-finished translation still builds.
"""
import html
import json
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
I18N = os.path.join(ROOT, "site-i18n")

SITE = "https://autumn1rain.github.io/karina-v3-k1/"
REPO = "https://github.com/autumn1rain/karina-v3-k1"
REPO_V1 = "https://github.com/autumn1rain/karina-v1"
LATEST = REPO + "/releases/latest"
CHAT = "https://t.me/k5fwmod"
FAGCI = "https://github.com/fagci/uv-k5-firmware-fagci-mod"
TOOL_LINKS = [
    "https://armel.github.io/uvstudio/#flash",
    "https://en.qsfj.com/support/downloads/8483",
    "https://github.com/sq5bpf/k5prog",
    "https://egzumer.github.io/uvtools",
    "https://github.com/ERuban/k5k1prog-mac",
]

LANGS = [("en", "English", ""), ("ru", "Русский", "ru/"), ("es", "Español", "es/"),
         ("de", "Deutsch", "de/"), ("zh", "中文", "zh/")]

STRINGS = {
    "title": "Karina firmware for Quansheng UV-K5 V3 and UV-K1",
    "description": "Karina (autumn rain) firmware for the Quansheng UV-K5 V3, UV-K1 and "
                   "UV-K1(8): spectrum analyser, FM radio, scan lists. Free download.",
    "tagline": "Community firmware for the Quansheng UV-K5 (V3), UV-K1 and UV-K1(8)",
    "lede": "Karina adds a spectrum analyser, FM broadcast radio, flexible scanning and a "
            "reworked menu to the radio you already own. Free, open licence, no accounts.",
    "download": "Download",
    "version_note": "Latest release on GitHub",
    "source": "Source code",
    "chat": "Telegram chat",
    "warning_h": "Before you flash anything",
    "warning": "Firmware built for one hardware version bricks another one. Check which radio "
               "you have, and back up your calibration first — it is unique to your radio and "
               "nobody can give it back to you.",
    "radios_h": "Which radio do I have?",
    "radios_lede": "Switch the radio off, hold PTT and switch it on: the display shows the "
                   "bootloader version. Its first digit tells you the hardware version.",
    "radios_cols": ["Bootloader starts with", "Radio", "Karina build"],
    "radios_rows": [
        ["2, 3, 4, 5", "UV-K5 V1", "karina-v1 (separate repository)"],
        ["1", "UV-K5 V2", "not supported"],
        ["7", "UV-K5 V3, UV-K1, UV-K1(8)", "this repository"],
    ],
    "radios_note": "V1 radios carry no marking; V2 and V3 usually have one on the sticker "
                   "under the battery.",
    "v1_note": "Got the older UV-K5 V1? It has a build of its own, in a separate repository:",
    "features_h": "What Karina adds",
    "features": [
        ("Spectrum analyser",
         "Band presets, a free-entry mode, live capture of the active frequency, a blacklist "
         "for noisy channels, and controls for attenuator, AGC and squelch."),
        ("Scanning that behaves",
         "Scan lists, priority channels checked during the scan, and any channel skipped on "
         "the fly by switching its attenuator on."),
        ("Subtone scan",
         "Scan CTCSS/DCS tones on the current frequency and store the one that was found as "
         "the transmit subtone."),
        ("FM broadcast radio",
         "Station search with memories, resumed automatically five seconds after a signal on "
         "the working channel disappears."),
        ("Attenuator in three steps",
         "ATT1, ATT2 and ATT3 per frequency or channel — useful next to a strong transmitter "
         "and for skipping channels while scanning."),
        ("Power, battery and extras",
         "HIGH / MID / LOW TX power, a reworked battery saver, dynamic volume, a frequency "
         "and power randomizer, NOAA, AM and USB modulation."),
    ],
    "install_h": "Install",
    "install_lede": "The short version. The full procedure with screenshots is in the "
                    "installation guide below.",
    "install": [
        "Back up your calibration and configuration while the radio still runs its current "
        "firmware.",
        "Switch the radio off, hold <b>PTT</b> and switch it on — that is flash mode.",
        "Flash the file for your radio with any of the tools below.",
        "Clear the memory: switch off, then switch on holding <b>PTT + EXIT</b> for about two "
        "seconds.",
        "Write your calibration back, then write the Karina calibration from the release.",
        "Reset the radio: <b>MENU → RESET → VFO</b>.",
    ],
    "tools_h": "Flashing tools",
    "tools_cols": ["Tool", "Platform", "File"],
    "tools_rows": [
        ["UV Studio", "web (Chrome, Edge, Opera, Brave)", "see the tool"],
        ["Official Quansheng updater", "Windows", "*.packed.bin"],
        ["k5prog", "Linux, macOS", "*.bin"],
        ["uvtools", "web (Chrome, Edge)", "see the tool"],
        ["K5K1 Prog", "macOS", "*.bin or *.packed.bin"],
    ],
    "tools_note": "Check that your tool supports your radio before you start. You do this at "
                  "your own risk.",
    "docs_h": "Documentation",
    "docs_lede": "The installation guide covers flashing and CHIRP; the manual describes every "
                 "menu item and key.",
    "docs_install": "Installation guide and CHIRP",
    "docs_manual": "Firmware manual",
    "docs_ru": "Russian (original)",
    "docs_en": "English",
    "faq_h": "Questions",
    "faq": [
        ("Can I flash this into a UV-K5 V1?",
         "No. V1 has a different processor and a different bootloader; the wrong firmware "
         "bricks the radio. V1 owners need the karina-v1 build."),
        ("Do I really need the calibration backup?",
         "Yes. Calibration holds your own radio's TX power and battery data. It is not in any "
         "release and nobody can restore it for you."),
        ("Can I keep my settings from another firmware?",
         "No. Only a configuration saved from an earlier Karina version can be written back. "
         "Channels can be moved with CHIRP."),
        ("The radio asks for a code after I wrote settings from CHIRP.",
         "That happens when a side key is left as NONE. Fill in all four side-key assignments "
         "(short and long press for both keys) before writing."),
        ("Where do I ask for help?",
         "In the Telegram chat, in the comments. Please say which radio and which firmware "
         "version you have."),
    ],
    "footer_base": "Karina is based on fagci's UV-K5 mod (v1.2.1) and the open firmware work of "
                   "Dual Tachyon, OneOfEleven, muzkr, armel and others.",
    "footer_license": "Licensed under the Apache License 2.0.",
    "footer_lang": "Language",
    "translation_note": "Translated from English. The English page is the authoritative version.",
}

CSS = """
:root {
  --bg:#ffffff; --bg-soft:#f5f6f9; --card:#ffffff; --text:#171a21; --muted:#5a6070;
  --border:#e4e6ec; --accent:#4b63d8; --accent-text:#ffffff; --ok:#1f9d55; --no:#c0392b;
  --radius:14px; color-scheme: light dark;
}
@media (prefers-color-scheme: dark) {
  :root { --bg:#10131c; --bg-soft:#161a26; --card:#1a1f2d; --text:#e9ebf2; --muted:#9aa1b4;
          --border:#262c3c; --accent:#8094ff; --accent-text:#10131c; --ok:#3ccf7e; --no:#ff6b5b; }
}
* { box-sizing:border-box; }
html { scroll-behavior:smooth; }
body { margin:0; background:var(--bg); color:var(--text);
  font:17px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei",
  Roboto, "Helvetica Neue", Arial, sans-serif; }
.wrap { max-width:980px; margin:0 auto; padding:0 20px; }
a { color:var(--accent); }
header.top { display:flex; justify-content:space-between; align-items:center; gap:16px;
  padding:18px 0; border-bottom:1px solid var(--border); }
.brand { font-weight:700; letter-spacing:-0.01em; }
.brand span { color:var(--muted); font-weight:400; }
nav a { margin-left:14px; color:var(--muted); text-decoration:none; font-size:15px; }
nav a:hover { color:var(--text); }
.hero { display:flex; gap:36px; align-items:center; padding:54px 0 40px; }
.hero-text { flex:1 1 auto; }
.hero img { width:auto; height:auto; max-height:380px; flex:0 0 auto; }
h1 { font-size:38px; line-height:1.15; letter-spacing:-0.02em; margin:0 0 10px; }
.tagline { color:var(--muted); font-size:19px; margin:0 0 18px; }
.cta { display:flex; flex-wrap:wrap; gap:10px; align-items:center; margin:22px 0 8px; }
.btn { display:inline-block; padding:11px 20px; border-radius:10px; text-decoration:none;
  font-weight:600; background:var(--accent); color:var(--accent-text); }
.btn.ghost { background:transparent; color:var(--text); border:1px solid var(--border); }
.sub { color:var(--muted); font-size:14px; margin:4px 0 0; }
section { padding:40px 0; border-top:1px solid var(--border); }
section h2 { font-size:28px; letter-spacing:-0.01em; margin:0 0 14px; }
section p.lede { color:var(--muted); margin:0 0 18px; }
.warn { border:1px solid var(--border); border-left:4px solid var(--no); background:var(--bg-soft);
  border-radius:var(--radius); padding:16px 18px; margin:26px 0 0; }
.warn b { display:block; margin-bottom:4px; }
.hint { border:1px solid var(--border); border-left:4px solid var(--accent);
  background:var(--bg-soft); border-radius:var(--radius); padding:13px 16px; margin:16px 0 0; }
.warn p { margin:0; color:var(--muted); }
.cards { display:grid; grid-template-columns:repeat(3,1fr); gap:16px; }
.card { background:var(--card); border:1px solid var(--border); border-radius:var(--radius);
  padding:18px; }
.card h3 { margin:0 0 6px; font-size:17px; }
.card p { margin:0; color:var(--muted); font-size:15.5px; }
table { width:100%; border-collapse:collapse; margin:4px 0 10px; font-size:15.5px; }
th, td { border-bottom:1px solid var(--border); padding:9px 10px; text-align:left;
  vertical-align:top; }
th { color:var(--muted); font-weight:600; font-size:14px; }
ol.steps { padding-left:20px; margin:0; }
ol.steps li { margin:0 0 10px; }
.qa { display:grid; grid-template-columns:1fr 1fr; gap:14px 28px; }
.qa h3 { font-size:17px; margin:0 0 4px; }
.qa p { margin:0; color:var(--muted); font-size:15.5px; }
.shots { display:flex; gap:14px; flex-wrap:wrap; margin-top:10px; }
.shots img { max-width:100%; border:1px solid var(--border); border-radius:8px; }
footer { border-top:1px solid var(--border); padding:28px 0 46px; color:var(--muted);
  font-size:14.5px; }
footer p { margin:0 0 8px; }
.langs a { margin-right:12px; }
.anchor { margin-left:0.35em; color:var(--muted); font-weight:400; text-decoration:none;
  opacity:0; transition:opacity .15s ease; }
h2:hover .anchor { opacity:0.45; }
.anchor:hover, .anchor:focus-visible { opacity:1; color:var(--accent); }
section[id] { scroll-margin-top:18px; }
@media (hover:none) { .anchor { opacity:0.3; } }
@media (max-width:860px) {
  .cards { grid-template-columns:1fr; }
  .qa { grid-template-columns:1fr; }
  .hero { flex-direction:column-reverse; align-items:flex-start; padding-top:34px; }
  .hero img { max-height:260px; }
  h1 { font-size:30px; }
}
"""


def e(s):
    return html.escape(str(s), quote=True)


def load(lang):
    t = dict(STRINGS)
    path = os.path.join(I18N, f"{lang}.json")
    if lang != "en" and os.path.exists(path):
        t.update({k: v for k, v in json.load(open(path)).items() if v})
    return t


def table(cols, rows):
    head = "".join(f"<th>{e(c)}</th>" for c in cols)
    body = "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>" for r in rows)
    return f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"


def tools_table(cols, rows):
    """Same as table(), but the tool name in the first column links to the tool."""
    head = "".join(f"<th>{e(c)}</th>" for c in cols)
    body = ""
    for i, r in enumerate(rows):
        url = TOOL_LINKS[i] if i < len(TOOL_LINKS) else ""
        first = f'<a href="{url}">{e(r[0])}</a>' if url else e(r[0])
        rest = "".join(f"<td>{e(c)}</td>" for c in r[1:])
        body += f"<tr><td>{first}</td>{rest}</tr>"
    return f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"


def page(lang, label, prefix, t):
    base = "../" if prefix else ""
    anchor_label = t.get("anchor", "Link to this section")

    def h2(sec, text):
        return (f'<h2>{e(text)}<a class="anchor" href="#{sec}" '
                f'aria-label="{e(anchor_label)}">#</a></h2>')

    others = "".join(
        f'<a href="{SITE}{p}">{e(n)}</a>' for code, n, p in LANGS if code != lang)
    cards = "".join(
        f'<div class="card"><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in t["features"])
    steps = "".join(f"<li>{s}</li>" for s in t["install"])
    faq = "".join(f"<div><h3>{e(q)}</h3><p>{e(a)}</p></div>" for q, a in t["faq"])
    radios = table(t["radios_cols"], t["radios_rows"])
    tools = tools_table(t["tools_cols"], t["tools_rows"])
    note = (f'<p class="sub">{e(t["translation_note"])}</p>' if lang != "en" else "")
    alts = "".join(
        f'<link rel="alternate" hreflang="{c}" href="{SITE}{p}">' for c, _, p in LANGS)

    faq_ld = json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]],
    }, ensure_ascii=False)
    app_ld = json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication",
        "name": "Karina firmware", "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "Quansheng UV-K5 V3, UV-K1", "url": SITE,
        "downloadUrl": LATEST, "license": "https://www.apache.org/licenses/LICENSE-2.0",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
    }, ensure_ascii=False)

    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["description"])}">
<link rel="canonical" href="{SITE}{prefix}">
{alts}<link rel="alternate" hreflang="x-default" href="{SITE}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(t["title"])}">
<meta property="og:description" content="{e(t["description"])}">
<meta property="og:url" content="{SITE}{prefix}">
<meta property="og:image" content="{SITE}assets/radio-k1.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#4b63d8">
<link rel="stylesheet" href="{base}assets/style.css">
<script type="application/ld+json">{faq_ld}</script>
<script type="application/ld+json">{app_ld}</script>
</head>
<body>
<div class="wrap">
<header class="top">
  <div class="brand">Karina <span>— autumn rain</span></div>
  <nav>
    <a href="#radios">{e(t["radios_h"])}</a>
    <a href="#install">{e(t["install_h"])}</a>
    <a href="#docs">{e(t["docs_h"])}</a>
    <a href="{REPO}">GitHub</a>
  </nav>
</header>

<div class="hero">
  <div class="hero-text">
    <h1>{e(t["tagline"])}</h1>
    <p class="tagline">{e(t["lede"])}</p>
    <div class="cta">
      <a class="btn" href="{LATEST}">{e(t["download"])}</a>
      <a class="btn ghost" href="{REPO}">{e(t["source"])}</a>
      <a class="btn ghost" href="{CHAT}">{e(t["chat"])}</a>
    </div>
    <p class="sub">{e(t["version_note"])}</p>
    {note}
  </div>
  <img src="{base}assets/radio-k1.png" alt="Quansheng UV-K1">
</div>

<div class="warn">
  <b>{e(t["warning_h"])}</b>
  <p>{e(t["warning"])}</p>
</div>

<section id="radios">
  {h2("radios", t["radios_h"])}
  <p class="lede">{e(t["radios_lede"])}</p>
  {radios}
  <p class="sub">{e(t["radios_note"])}</p>
  <p class="hint">{e(t["v1_note"])} <a href="{REPO_V1}">autumn1rain/karina-v1</a></p>
</section>

<section id="features">
  {h2("features", t["features_h"])}
  <div class="cards">{cards}</div>
  <div class="shots"><img src="{base}assets/spectrum.png" alt="Spectrum analyser screen"></div>
</section>

<section id="install">
  {h2("install", t["install_h"])}
  <p class="lede">{e(t["install_lede"])}</p>
  <ol class="steps">{steps}</ol>
  <h3>{e(t["tools_h"])}</h3>
  {tools}
  <p class="sub">{e(t["tools_note"])}</p>
</section>

<section id="docs">
  {h2("docs", t["docs_h"])}
  <p class="lede">{e(t["docs_lede"])}</p>
  <table><thead><tr><th>&nbsp;</th><th>{e(t["docs_ru"])}</th><th>{e(t["docs_en"])}</th></tr></thead>
  <tbody>
  <tr><td>{e(t["docs_install"])}</td>
      <td><a href="{REPO}/blob/main/karina-v3-k1-install.pdf">PDF</a></td>
      <td><a href="{REPO}/blob/main/karina-v3-k1-install-en.pdf">PDF</a></td></tr>
  <tr><td>{e(t["docs_manual"])}</td>
      <td><a href="{REPO}/blob/main/karina-v3-k1-manual.pdf">PDF</a></td>
      <td><a href="{REPO}/blob/main/karina-v3-k1-manual-en.pdf">PDF</a></td></tr>
  </tbody></table>
</section>

<section id="faq">
  {h2("faq", t["faq_h"])}
  <div class="qa">{faq}</div>
</section>

<footer>
  <p>{e(t["footer_base"])} <a href="{FAGCI}">fagci/uv-k5-firmware-fagci-mod</a></p>
  <p>{e(t["footer_license"])} © 2026 autumn1rain.</p>
  <p class="langs">{e(t["footer_lang"])}: {others}</p>
</footer>
</div>
</body>
</html>
"""


def main():
    os.makedirs(os.path.join(DOCS, "assets"), exist_ok=True)
    open(os.path.join(DOCS, "assets", "style.css"), "w").write(CSS)
    open(os.path.join(DOCS, ".nojekyll"), "w").write("")
    written = []
    for lang, label, prefix in LANGS:
        t = load(lang)
        out_dir = os.path.join(DOCS, prefix.strip("/")) if prefix else DOCS
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "index.html")
        open(path, "w").write(page(lang, label, prefix, t))
        written.append(os.path.relpath(path, ROOT))
        title_len = len(t["title"])
        desc_len = len(t["description"])
        print(f"{os.path.relpath(path, ROOT)}  title {title_len}  desc {desc_len}")
    urls = "".join(
        f"<url><loc>{SITE}{p}</loc><xhtml:link rel='alternate' hreflang='{c}' "
        f"href='{SITE}{p}'/></url>" for c, _, p in LANGS)
    open(os.path.join(DOCS, "sitemap.xml"), "w").write(
        "<?xml version='1.0' encoding='UTF-8'?>"
        "<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9' "
        "xmlns:xhtml='http://www.w3.org/1999/xhtml'>" + urls + "</urlset>")
    open(os.path.join(DOCS, "robots.txt"), "w").write(
        f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
    print(f"wrote {len(written)} pages, sitemap.xml, robots.txt")


if __name__ == "__main__":
    main()
