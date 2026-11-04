<div align="center">

# Karina

**Альтернативная прошивка для Quansheng UV-K5 (V3), UV-K1 и UV-K1(8)**

<p align="center">
<a href="README.md">English</a> |
<a href="README_ES.md">Español</a> |
<a href="README_DE.md">Deutsch</a> |
<a href="README_ZH.md">中文</a>
</p>

*Это перевод; авторитетной версией остаётся английский README.*

[![Latest release](https://img.shields.io/github/v/release/autumn1rain/karina-v3-k1?label=release)](https://github.com/autumn1rain/karina-v3-k1/releases/latest)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)
[![Radios](https://img.shields.io/badge/radios-UV--K5%20V3%20%C2%B7%20UV--K1-success)](#какая-у-меня-рация)

[**Скачать**](https://github.com/autumn1rain/karina-v3-k1/releases/latest) ·
[Руководство по установке](karina-v3-k1-install.pdf) ·
[Руководство пользователя](karina-v3-k1-manual.pdf) ·
[Чат в Telegram](https://t.me/k5fwmod) ·
[Сайт](https://autumn1rain.github.io/karina-v3-k1/ru/)

</div>

---

> [!WARNING]
> Прошивка, собранная под одну аппаратную версию, превратит другую в **кирпич**. Прежде чем
> что-либо прошивать, проверьте, какая у вас рация, и сначала сохраните резервную копию
> калибровки — она уникальна для вашей рации, и вернуть её вам никто не сможет.

Karina (*осенний дождь*) — это прошивка от сообщества для Quansheng UV-K5 (V3), UV-K1 и
UV-K1(8). Она основана на [моде fagci для UV-K5](https://github.com/fagci/uv-k5-firmware-fagci-mod)
(v1.2.1).

Владельцам более старых **UV-K5 V1** нужна отдельная сборка:
[autumn1rain/karina-v1](https://github.com/autumn1rain/karina-v1).

## Какая у меня рация?

Выключите рацию, затем зажмите **PTT** и включите её: на дисплее появится версия загрузчика.
Его первая цифра говорит об аппаратной версии.

| Загрузчик начинается с | Рация | Сборка Karina |
| --- | --- | --- |
| `2`, `3`, `4`, `5` | UV-K5 **V1** | [karina-v1](https://github.com/autumn1rain/karina-v1) |
| `1` | UV-K5 **V2** | не поддерживается |
| `7` | UV-K5 **V3**, UV-K1, UV-K1(8) | этот репозиторий |

На рациях V1 маркировки нет; у V2 и V3 она обычно есть на наклейке под аккумулятором.

## Скачать

Всё лежит на [странице релизов](https://github.com/autumn1rain/karina-v3-k1/releases/latest).

| Файл | Рация | Чем прошивать |
| --- | --- | --- |
| `karina-v3.bin` | UV-K5 V3 | k5prog, K5K1 Prog, веб-прошивальщики |
| `karina-v3.packed.bin` | UV-K5 V3 | официальная утилита обновления Quansheng |
| `karina-k1.bin` | UV-K1, UV-K1(8) | k5prog, K5K1 Prog, веб-прошивальщики |
| `karina-k1.packed.bin` | UV-K1, UV-K1(8) | официальная утилита обновления Quansheng |
| `calibration.bin` | обе | калибровка, входящая в этот релиз |

## Установка

Ниже — краткий вариант. Полная процедура со скриншотами и разделом про CHIRP описана в
[karina-v3-k1-install.pdf](karina-v3-k1-install.pdf).

1. **Сначала сделайте резервную копию.** Считайте и сохраните калибровку и конфигурацию
   рации, пока она ещё работает на текущей прошивке. В калибровке хранятся данные о мощности
   передатчика и аккумуляторе именно вашей рации — её потеря стоит вам дальности и верных показаний.
2. **Войдите в режим прошивки.** Выключите рацию, зажмите **PTT**, включите её.
3. **Прошейте** файл для вашей рации любым из инструментов ниже.
4. **Очистите память.** Выключите рацию, затем включите её, удерживая **PTT + EXIT** примерно
   две секунды.
5. **Запишите калибровку обратно**, затем запишите калибровку Karina из релиза.
6. **Сбросьте рацию**: `MENU` → `RESET` → `VFO`.

| Инструмент | Платформа | Файл |
| --- | --- | --- |
| [UV Studio](https://armel.github.io/uvstudio/#flash) | веб (Chrome, Edge, Opera, Brave) | смотрите в самом инструменте |
| [Официальная утилита обновления Quansheng](https://en.qsfj.com/support/downloads/8483) | Windows | `*.packed.bin` |
| [k5prog](https://github.com/sq5bpf/k5prog) — `./k5prog -F -YYY -b <file>.bin` | Linux, macOS | `*.bin` |
| [uvtools](https://egzumer.github.io/uvtools) | веб (Chrome, Edge) | смотрите в самом инструменте |
| [K5K1 Prog](https://github.com/ERuban/k5k1prog-mac) | macOS | `*.bin` или `*.packed.bin` |

Перед началом убедитесь, что ваш инструмент поддерживает вашу рацию. Всё это вы делаете на свой страх и риск.

## Каналы и CHIRP

Каналы редактируются в [CHIRP](https://chirpmyradio.com/) с модулем-драйвером Karina либо в
любом инструменте, который понимает такую же структуру каналов. Файлы конфигурации от
**других** прошивок не подходят: записать обратно можно только конфигурацию, сохранённую из
более ранней версии Karina.

## Документация

| Документ | Русский | Английский |
| --- | --- | --- |
| Установка и CHIRP | [karina-v3-k1-install.pdf](karina-v3-k1-install.pdf) | [karina-v3-k1-install-en.pdf](karina-v3-k1-install-en.pdf) |
| Руководство по прошивке | [karina-v3-k1-manual.pdf](karina-v3-k1-manual.pdf) | [karina-v3-k1-manual-en.pdf](karina-v3-k1-manual-en.pdf) |

Вопросы и сообщения об ошибках — в [чат Telegram](https://t.me/k5fwmod), в комментарии.

## Благодарности

Karina опирается на работу людей, которые открыли эту рацию:

- [Dual Tachyon](https://github.com/DualTachyon) — исходная открытая прошивка
- [Mikhail (fagci)](https://github.com/fagci) — мод, на котором основана Karina
- [OneOfEleven](https://github.com/OneOfEleven), [muzkr](https://github.com/muzkr),
  [armel](https://github.com/armel), [Andrej](https://github.com/Tunas1337) — работа над прошивкой и инструменты
- [ERuban](https://github.com/ERuban) (@vkusni) — [K5K1 Prog](https://github.com/ERuban/k5k1prog-mac) для macOS
- Документация и тестирование: DmitroBuka (@DmitrBukatov), Kolyan (@Kolyanuch), PunkTracker,
  Avers (@aversreg), Киловольт Киловольтович, Ivan (@s_ivan96), Руслан Румянцев
- QUANSHENG и все остальные, кто помогал

## Лицензия

```
Copyright 2023 Dual Tachyon <https://github.com/DualTachyon>
Copyright 2023 fagci <https://github.com/fagci>
Copyright 2023 OneOfEleven <https://github.com/OneOfEleven>
Copyright 2025 muzkr <https://github.com/muzkr>
Copyright 2025 armel <https://github.com/armel>
Modifications Copyright 2026 autumn1rain <https://github.com/autumn1rain>
```

Распространяется по лицензии Apache License, версия 2.0. Полный текст и список
правообладателей — в [LICENSE](LICENSE).
