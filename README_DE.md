<div align="center">

# Karina

**Custom-Firmware für Quansheng UV-K5 (V3), UV-K1 und UV-K1(8)**

<p align="center">
<a href="README.md">English</a> |
<a href="README_RU.md">Русский</a> |
<a href="README_ES.md">Español</a> |
<a href="README_ZH.md">中文</a>
</p>

[![Latest release](https://img.shields.io/github/v/release/autumn1rain/karina-v3-k1?label=release)](https://github.com/autumn1rain/karina-v3-k1/releases/latest)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)
[![Radios](https://img.shields.io/badge/radios-UV--K5%20V3%20%C2%B7%20UV--K1-success)](#welches-funkgerät-habe-ich)

[**Download**](https://github.com/autumn1rain/karina-v3-k1/releases/latest) ·
[Installationsanleitung](karina-v3-k1-install.pdf) ·
[Handbuch](karina-v3-k1-manual.pdf) ·
[Telegram-Chat](https://t.me/k5fwmod) ·
[Website](https://autumn1rain.github.io/karina-v3-k1/)

</div>

---

*Dies ist eine Übersetzung. Maßgeblich ist die englische Fassung der README.*

> [!WARNING]
> Firmware für die eine Hardware-Version macht eine andere **unbrauchbar**. Prüfen Sie vor dem
> Flashen, welches Funkgerät Sie haben, und sichern Sie zuerst Ihre Kalibrierung — sie ist für
> Ihr Gerät einmalig, und niemand kann sie Ihnen zurückgeben.

Karina (*autumn rain*) ist eine Community-Firmware für Quansheng UV-K5 (V3), UV-K1 und
UV-K1(8). Sie basiert auf [fagcis UV-K5-Mod](https://github.com/fagci/uv-k5-firmware-fagci-mod)
(v1.2.1).

Besitzer des älteren **UV-K5 V1** brauchen den separaten Build:
[autumn1rain/karina-v1](https://github.com/autumn1rain/karina-v1).

## Welches Funkgerät habe ich?

Schalten Sie das Funkgerät aus, halten Sie dann **PTT** gedrückt und schalten Sie es ein: Im
Display erscheint die Bootloader-Version. Deren erste Ziffer nennt Ihnen die Hardware-Version.

| Bootloader beginnt mit | Funkgerät | Karina-Build |
| --- | --- | --- |
| `2`, `3`, `4`, `5` | UV-K5 **V1** | [karina-v1](https://github.com/autumn1rain/karina-v1) |
| `1` | UV-K5 **V2** | nicht unterstützt |
| `7` | UV-K5 **V3**, UV-K1, UV-K1(8) | dieses Repository |

V1-Geräte tragen keine Kennzeichnung; V2 und V3 haben meist eine auf dem Aufkleber unter dem Akku.

## Download

Alles finden Sie auf der [Releases-Seite](https://github.com/autumn1rain/karina-v3-k1/releases/latest).

| Datei | Funkgerät | Verwenden mit |
| --- | --- | --- |
| `karina-v3.bin` | UV-K5 V3 | k5prog, K5K1 Prog, Web-Flasher |
| `karina-v3.packed.bin` | UV-K5 V3 | dem offiziellen Quansheng-Updater |
| `karina-k1.bin` | UV-K1, UV-K1(8) | k5prog, K5K1 Prog, Web-Flasher |
| `karina-k1.packed.bin` | UV-K1, UV-K1(8) | dem offiziellen Quansheng-Updater |
| `calibration.bin` | beide | der mit diesem Release gelieferten Kalibrierung |

## Installation

Nachstehend die Kurzfassung. Das vollständige Vorgehen, mit Screenshots und dem CHIRP-Teil, steht in
[karina-v3-k1-install.pdf](karina-v3-k1-install.pdf).

1. **Zuerst sichern.** Lesen und speichern Sie Kalibrierung und Konfiguration Ihres Funkgeräts,
   solange es noch mit der bisherigen Firmware läuft. Die Kalibrierung enthält die Sendeleistungs-
   und Akkudaten Ihres eigenen Geräts — ihr Verlust kostet Sie Reichweite und korrekte Anzeigen.
2. **In den Flash-Modus wechseln.** Funkgerät ausschalten, **PTT** halten, einschalten.
3. **Flashen** Sie die Datei für Ihr Funkgerät mit einem der Werkzeuge unten.
4. **Speicher löschen.** Schalten Sie das Funkgerät aus und dann wieder ein, während Sie
   **PTT + EXIT** etwa zwei Sekunden lang halten.
5. **Schreiben Sie die Kalibrierung zurück**, danach die Karina-Kalibrierung aus dem Release.
6. **Setzen Sie das Funkgerät zurück**: `MENU` → `RESET` → `VFO`.

| Werkzeug | Plattform | Datei |
| --- | --- | --- |
| [UV Studio](https://armel.github.io/uvstudio/#flash) | Web (Chrome, Edge, Opera, Brave) | siehe Werkzeug |
| [Offizieller Quansheng-Updater](https://en.qsfj.com/support/downloads/8483) | Windows | `*.packed.bin` |
| [k5prog](https://github.com/sq5bpf/k5prog) — `./k5prog -F -YYY -b <file>.bin` | Linux, macOS | `*.bin` |
| [uvtools](https://egzumer.github.io/uvtools) | Web (Chrome, Edge) | siehe Werkzeug |
| [K5K1 Prog](https://github.com/ERuban/k5k1prog-mac) | macOS | `*.bin` oder `*.packed.bin` |

Prüfen Sie vor dem Start, ob Ihr Werkzeug Ihr Funkgerät unterstützt. Sie handeln auf eigenes Risiko.

## Kanäle und CHIRP

Kanäle werden in [CHIRP](https://chirpmyradio.com/) mit dem Karina-Treibermodul bearbeitet, oder in
jedem Werkzeug, das dasselbe Kanal-Layout versteht. Konfigurationsdateien **anderer** Firmware
passen nicht: Nur eine Konfiguration, die aus einer früheren Karina-Version gespeichert wurde, lässt
sich zurückschreiben.

## Dokumentation

| Dokument | Russisch | Englisch |
| --- | --- | --- |
| Installation und CHIRP | [karina-v3-k1-install.pdf](karina-v3-k1-install.pdf) | [karina-v3-k1-install-en.pdf](karina-v3-k1-install-en.pdf) |
| Firmware-Handbuch | [karina-v3-k1-manual.pdf](karina-v3-k1-manual.pdf) | [karina-v3-k1-manual-en.pdf](karina-v3-k1-manual-en.pdf) |

Fragen und Meldungen gehören in den [Telegram-Chat](https://t.me/k5fwmod), in die Kommentare.

## Danksagungen

Karina baut auf der Arbeit der Leute auf, die dieses Funkgerät geöffnet haben:

- [Dual Tachyon](https://github.com/DualTachyon) — die ursprüngliche offene Firmware
- [Mikhail (fagci)](https://github.com/fagci) — der Mod, auf dem Karina basiert
- [OneOfEleven](https://github.com/OneOfEleven), [muzkr](https://github.com/muzkr),
  [armel](https://github.com/armel), [Andrej](https://github.com/Tunas1337) — Firmware-Arbeit und Werkzeuge
- [ERuban](https://github.com/ERuban) (@vkusni) — [K5K1 Prog](https://github.com/ERuban/k5k1prog-mac) für macOS
- Dokumentation und Tests: DmitroBuka (@DmitrBukatov), Kolyan (@Kolyanuch), PunkTracker,
  Avers (@aversreg), Киловольт Киловольтович, Ivan (@s_ivan96), Руслан Румянцев
- QUANSHENG und alle anderen, die geholfen haben

## Lizenz

```
Copyright 2023 Dual Tachyon <https://github.com/DualTachyon>
Copyright 2023 fagci <https://github.com/fagci>
Copyright 2023 OneOfEleven <https://github.com/OneOfEleven>
Copyright 2025 muzkr <https://github.com/muzkr>
Copyright 2025 armel <https://github.com/armel>
Modifications Copyright 2026 autumn1rain <https://github.com/autumn1rain>
```

Lizenziert unter der Apache License, Version 2.0. Den vollständigen Text und die Liste der
Rechteinhaber finden Sie in [LICENSE](LICENSE).
