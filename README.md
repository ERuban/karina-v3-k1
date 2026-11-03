<div align="center">

# Karina

**Custom firmware for the Quansheng UV-K5 (V3), UV-K1 and UV-K1(8)**

<p align="center">
<a href="README_RU.md">Русский</a> |
<a href="README_ES.md">Español</a> |
<a href="README_DE.md">Deutsch</a> |
<a href="README_ZH.md">中文</a>
</p>

[![Latest release](https://img.shields.io/github/v/release/autumn1rain/karina-v3-k1?label=release)](https://github.com/autumn1rain/karina-v3-k1/releases/latest)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)
[![Radios](https://img.shields.io/badge/radios-UV--K5%20V3%20%C2%B7%20UV--K1-success)](#which-radio-do-i-have)

[**Download**](https://github.com/autumn1rain/karina-v3-k1/releases/latest) ·
[Installation guide](karina-v3-k1-install.pdf) ·
[Manual](karina-v3-k1-manual.pdf) ·
[Telegram chat](https://t.me/k5fwmod) ·
[Website](https://autumn1rain.github.io/karina-v3-k1/)

</div>

---

> [!WARNING]
> Firmware built for one hardware version will **brick** another one. Check which radio you
> have before you flash anything, and back up your calibration first — it is unique to your
> radio and nobody can give it back to you.

Karina (*autumn rain*) is a community firmware for the Quansheng UV-K5 (V3), UV-K1 and
UV-K1(8). It is based on [fagci's UV-K5 mod](https://github.com/fagci/uv-k5-firmware-fagci-mod)
(v1.2.1).

Owners of the older **UV-K5 V1** need the separate build:
[autumn1rain/karina-v1](https://github.com/autumn1rain/karina-v1).

## Which radio do I have?

Switch the radio off, then hold **PTT** and switch it on: the display shows the bootloader
version. Its first digit tells you the hardware version.

| Bootloader starts with | Radio | Karina build |
| --- | --- | --- |
| `2`, `3`, `4`, `5` | UV-K5 **V1** | [karina-v1](https://github.com/autumn1rain/karina-v1) |
| `1` | UV-K5 **V2** | not supported |
| `7` | UV-K5 **V3**, UV-K1, UV-K1(8) | this repository |

V1 radios carry no marking; V2 and V3 usually have one on the sticker under the battery.

## Download

Everything is on the [releases page](https://github.com/autumn1rain/karina-v3-k1/releases/latest).

| File | Radio | Use it with |
| --- | --- | --- |
| `karina-v3.bin` | UV-K5 V3 | k5prog, K5K1 Prog, web flashers |
| `karina-v3.packed.bin` | UV-K5 V3 | the official Quansheng updater |
| `karina-k1.bin` | UV-K1, UV-K1(8) | k5prog, K5K1 Prog, web flashers |
| `karina-k1.packed.bin` | UV-K1, UV-K1(8) | the official Quansheng updater |
| `calibration.bin` | both | the calibration shipped with this release |

## Install

The short version is below. The full procedure, with screenshots and the CHIRP part, is in
[karina-v3-k1-install.pdf](karina-v3-k1-install.pdf).

1. **Back up first.** Read and save your radio's calibration and configuration while it still
   runs its current firmware. The calibration holds your own radio's TX power and battery
   data — losing it costs you range and correct readings.
2. **Enter flash mode.** Switch the radio off, hold **PTT**, switch it on.
3. **Flash** the file for your radio with any of the tools below.
4. **Clear the memory.** Switch the radio off, then switch it on holding **PTT + EXIT** for
   about two seconds.
5. **Write the calibration back**, then write the Karina calibration from the release.
6. **Reset the radio**: `MENU` → `RESET` → `VFO`.

| Tool | Platform | File |
| --- | --- | --- |
| [UV Studio](https://armel.github.io/uvstudio/#flash) | web (Chrome, Edge, Opera, Brave) | see the tool |
| [Official Quansheng updater](https://en.qsfj.com/support/downloads/8483) | Windows | `*.packed.bin` |
| [k5prog](https://github.com/sq5bpf/k5prog) — `./k5prog -F -YYY -b <file>.bin` | Linux, macOS | `*.bin` |
| [uvtools](https://egzumer.github.io/uvtools) | web (Chrome, Edge) | see the tool |
| [K5K1 Prog](https://github.com/ERuban/k5k1prog-mac) | macOS | `*.bin` or `*.packed.bin` |

Check that your tool supports your radio before you start. You do this at your own risk.

## Channels and CHIRP

Channels are edited in [CHIRP](https://chirpmyradio.com/) with the Karina driver module, or in
any tool that understands the same channel layout. Configuration files from **other** firmware
do not fit: only a configuration saved from an earlier Karina version can be written back.

## Documentation

| Document | Russian | English |
| --- | --- | --- |
| Installation and CHIRP | [karina-v3-k1-install.pdf](karina-v3-k1-install.pdf) | [karina-v3-k1-install-en.pdf](karina-v3-k1-install-en.pdf) |
| Firmware manual | [karina-v3-k1-manual.pdf](karina-v3-k1-manual.pdf) | [karina-v3-k1-manual-en.pdf](karina-v3-k1-manual-en.pdf) |

Questions and reports go to the [Telegram chat](https://t.me/k5fwmod), in the comments.

## Credits

Karina stands on the work of the people who opened this radio up:

- [Dual Tachyon](https://github.com/DualTachyon) — the original open firmware
- [Mikhail (fagci)](https://github.com/fagci) — the mod Karina is based on
- [OneOfEleven](https://github.com/OneOfEleven), [muzkr](https://github.com/muzkr),
  [armel](https://github.com/armel), [Andrej](https://github.com/Tunas1337) — firmware work and tools
- [ERuban](https://github.com/ERuban) (@vkusni) — [K5K1 Prog](https://github.com/ERuban/k5k1prog-mac) for macOS
- Documentation and testing: DmitroBuka (@DmitrBukatov), Kolyan (@Kolyanuch), PunkTracker,
  Avers (@aversreg), Киловольт Киловольтович, Ivan (@s_ivan96), Руслан Румянцев
- QUANSHENG, and everyone else who helped

## License

```
Copyright 2023 Dual Tachyon <https://github.com/DualTachyon>
Copyright 2023 fagci <https://github.com/fagci>
Copyright 2023 OneOfEleven <https://github.com/OneOfEleven>
Copyright 2025 muzkr <https://github.com/muzkr>
Copyright 2025 armel <https://github.com/armel>
Modifications Copyright 2026 autumn1rain <https://github.com/autumn1rain>
```

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full text and
the list of copyright holders.
