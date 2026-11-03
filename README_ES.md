<div align="center">

# Karina

**Firmware alternativo para los Quansheng UV-K5 (V3), UV-K1 y UV-K1(8)**

<p align="center">
<a href="README.md">English</a> |
<a href="README_RU.md">Русский</a> |
<a href="README_DE.md">Deutsch</a> |
<a href="README_ZH.md">中文</a>
</p>

*Esta es una traducción; el README en inglés es la versión autorizada.*

[![Latest release](https://img.shields.io/github/v/release/autumn1rain/karina-v3-k1?label=release)](https://github.com/autumn1rain/karina-v3-k1/releases/latest)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)
[![Radios](https://img.shields.io/badge/radios-UV--K5%20V3%20%C2%B7%20UV--K1-success)](#qué-radio-tengo)

[**Descargar**](https://github.com/autumn1rain/karina-v3-k1/releases/latest) ·
[Guía de instalación](karina-v3-k1-install.pdf) ·
[Manual](karina-v3-k1-manual.pdf) ·
[Chat de Telegram](https://t.me/k5fwmod) ·
[Sitio web](https://autumn1rain.github.io/karina-v3-k1/)

</div>

---

> [!WARNING]
> El firmware compilado para una versión de hardware **inutilizará** cualquier otra. Comprueba
> qué radio tienes antes de flashear nada y haz primero una copia de seguridad de tu
> calibración: es única de tu radio y nadie podrá devolvértela.

Karina (*lluvia de otoño*) es un firmware comunitario para los Quansheng UV-K5 (V3), UV-K1 y
UV-K1(8). Está basado en [el mod UV-K5 de fagci](https://github.com/fagci/uv-k5-firmware-fagci-mod)
(v1.2.1).

Los propietarios del antiguo **UV-K5 V1** necesitan la compilación aparte:
[autumn1rain/karina-v1](https://github.com/autumn1rain/karina-v1).

## ¿Qué radio tengo?

Apaga la radio, mantén pulsado **PTT** y enciéndela: la pantalla muestra la versión del
bootloader. Su primer dígito indica la versión de hardware.

| El bootloader empieza por | Radio | Compilación de Karina |
| --- | --- | --- |
| `2`, `3`, `4`, `5` | UV-K5 **V1** | [karina-v1](https://github.com/autumn1rain/karina-v1) |
| `1` | UV-K5 **V2** | no compatible |
| `7` | UV-K5 **V3**, UV-K1, UV-K1(8) | este repositorio |

Las radios V1 no llevan ninguna marca; las V2 y V3 suelen tenerla en la pegatina que hay bajo
la batería.

## Descarga

Todo está en la [página de releases](https://github.com/autumn1rain/karina-v3-k1/releases/latest).

| Archivo | Radio | Úsalo con |
| --- | --- | --- |
| `karina-v3.bin` | UV-K5 V3 | k5prog, K5K1 Prog, flasheadores web |
| `karina-v3.packed.bin` | UV-K5 V3 | el actualizador oficial de Quansheng |
| `karina-k1.bin` | UV-K1, UV-K1(8) | k5prog, K5K1 Prog, flasheadores web |
| `karina-k1.packed.bin` | UV-K1, UV-K1(8) | el actualizador oficial de Quansheng |
| `calibration.bin` | ambas | la calibración que acompaña a esta release |

## Instalación

Abajo tienes la versión resumida. El procedimiento completo, con capturas de pantalla y la
parte de CHIRP, está en [karina-v3-k1-install.pdf](karina-v3-k1-install.pdf).

1. **Haz primero una copia de seguridad.** Lee y guarda la calibración y la configuración de
   tu radio mientras todavía funciona con su firmware actual. La calibración contiene los
   datos de potencia de TX y de batería propios de tu radio: perderla te cuesta alcance y
   lecturas correctas.
2. **Entra en modo de flasheo.** Apaga la radio, mantén pulsado **PTT** y enciéndela.
3. **Flashea** el archivo correspondiente a tu radio con cualquiera de las herramientas de
   abajo.
4. **Borra la memoria.** Apaga la radio y vuelve a encenderla manteniendo pulsado
   **PTT + EXIT** durante unos dos segundos.
5. **Vuelve a escribir la calibración** y después escribe la calibración de Karina incluida en
   la release.
6. **Resetea la radio**: `MENU` → `RESET` → `VFO`.

| Herramienta | Plataforma | Archivo |
| --- | --- | --- |
| [UV Studio](https://armel.github.io/uvstudio/#flash) | web (Chrome, Edge, Opera, Brave) | consulta la herramienta |
| [Actualizador oficial de Quansheng](https://en.qsfj.com/support/downloads/8483) | Windows | `*.packed.bin` |
| [k5prog](https://github.com/sq5bpf/k5prog) — `./k5prog -F -YYY -b <file>.bin` | Linux, macOS | `*.bin` |
| [uvtools](https://egzumer.github.io/uvtools) | web (Chrome, Edge) | consulta la herramienta |
| [K5K1 Prog](https://github.com/ERuban/k5k1prog-mac) | macOS | `*.bin` o `*.packed.bin` |

Comprueba que tu herramienta admite tu radio antes de empezar. Lo haces bajo tu propia
responsabilidad.

## Canales y CHIRP

Los canales se editan en [CHIRP](https://chirpmyradio.com/) con el módulo de driver de Karina,
o en cualquier herramienta que entienda la misma estructura de canales. Los archivos de
configuración de **otros** firmwares no sirven: solo se puede volver a escribir una
configuración guardada desde una versión anterior de Karina.

## Documentación

| Documento | Ruso | Inglés |
| --- | --- | --- |
| Instalación y CHIRP | [karina-v3-k1-install.pdf](karina-v3-k1-install.pdf) | [karina-v3-k1-install-en.pdf](karina-v3-k1-install-en.pdf) |
| Manual del firmware | [karina-v3-k1-manual.pdf](karina-v3-k1-manual.pdf) | [karina-v3-k1-manual-en.pdf](karina-v3-k1-manual-en.pdf) |

Las preguntas y los informes van al [chat de Telegram](https://t.me/k5fwmod), en los comentarios.

## Créditos

Karina se apoya en el trabajo de quienes abrieron esta radio:

- [Dual Tachyon](https://github.com/DualTachyon) — el firmware abierto original
- [Mikhail (fagci)](https://github.com/fagci) — el mod en el que se basa Karina
- [OneOfEleven](https://github.com/OneOfEleven), [muzkr](https://github.com/muzkr),
  [armel](https://github.com/armel), [Andrej](https://github.com/Tunas1337) — trabajo de firmware y herramientas
- [ERuban](https://github.com/ERuban) (@vkusni) — [K5K1 Prog](https://github.com/ERuban/k5k1prog-mac) para macOS
- Documentación y pruebas: DmitroBuka (@DmitrBukatov), Kolyan (@Kolyanuch), PunkTracker,
  Avers (@aversreg), Киловольт Киловольтович, Ivan (@s_ivan96), Руслан Румянцев
- QUANSHENG y todos los demás que han ayudado

## Licencia

```
Copyright 2023 Dual Tachyon <https://github.com/DualTachyon>
Copyright 2023 fagci <https://github.com/fagci>
Copyright 2023 OneOfEleven <https://github.com/OneOfEleven>
Copyright 2025 muzkr <https://github.com/muzkr>
Copyright 2025 armel <https://github.com/armel>
Modifications Copyright 2026 autumn1rain <https://github.com/autumn1rain>
```

Distribuido bajo la Apache License, Versión 2.0. Consulta [LICENSE](LICENSE) para el texto
completo y la lista de titulares de los derechos de autor.
