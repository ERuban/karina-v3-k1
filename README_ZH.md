<div align="center">

# Karina

**适用于泉盛 Quansheng UV-K5 (V3)、UV-K1 和 UV-K1(8) 的第三方固件**

<p align="center">
<a href="README.md">English</a> |
<a href="README_RU.md">Русский</a> |
<a href="README_ES.md">Español</a> |
<a href="README_DE.md">Deutsch</a>
</p>

*本文为翻译版本，英文版 README 为权威版本。*

[![Latest release](https://img.shields.io/github/v/release/autumn1rain/karina-v3-k1?label=release)](https://github.com/autumn1rain/karina-v3-k1/releases/latest)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)
[![Radios](https://img.shields.io/badge/radios-UV--K5%20V3%20%C2%B7%20UV--K1-success)](#我有哪一款对讲机)

[**下载**](https://github.com/autumn1rain/karina-v3-k1/releases/latest) ·
[安装指南](karina-v3-k1-install.pdf) ·
[使用手册](karina-v3-k1-manual.pdf) ·
[Telegram 交流群](https://t.me/k5fwmod) ·
[网站](https://autumn1rain.github.io/karina-v3-k1/)

</div>

---

> [!WARNING]
> 为某一硬件版本编译的固件会把另一个版本**刷成砖**。在刷写任何固件之前，请先确认你手上
> 是哪一款对讲机，并且先备份校准数据 —— 它是你这台对讲机独有的，任何人都无法再还给你。

Karina（*秋雨*）是面向泉盛 Quansheng UV-K5 (V3)、UV-K1 和 UV-K1(8) 的社区固件。它基于
[fagci 的 UV-K5 mod](https://github.com/fagci/uv-k5-firmware-fagci-mod)（v1.2.1）开发。

较早的 **UV-K5 V1** 机型需要使用独立的版本：
[autumn1rain/karina-v1](https://github.com/autumn1rain/karina-v1)。

## 我有哪一款对讲机？

关闭对讲机，然后按住 **PTT** 再开机：屏幕会显示 Bootloader（引导程序）版本号。它的第一位
数字就表示硬件版本。

| Bootloader 开头数字 | 对讲机 | Karina 版本 |
| --- | --- | --- |
| `2`、`3`、`4`、`5` | UV-K5 **V1** | [karina-v1](https://github.com/autumn1rain/karina-v1) |
| `1` | UV-K5 **V2** | 不支持 |
| `7` | UV-K5 **V3**、UV-K1、UV-K1(8) | 本仓库 |

V1 机型没有任何标识；V2 和 V3 通常会在电池仓下方的标签上标明。

## 下载

所有文件都在[发布页面](https://github.com/autumn1rain/karina-v3-k1/releases/latest)。

| 文件 | 对讲机 | 配合使用的工具 |
| --- | --- | --- |
| `karina-v3.bin` | UV-K5 V3 | k5prog、K5K1 Prog、网页刷机工具 |
| `karina-v3.packed.bin` | UV-K5 V3 | 泉盛官方升级软件 |
| `karina-k1.bin` | UV-K1、UV-K1(8) | k5prog、K5K1 Prog、网页刷机工具 |
| `karina-k1.packed.bin` | UV-K1、UV-K1(8) | 泉盛官方升级软件 |
| `calibration.bin` | 两者通用 | 本次发布附带的校准数据 |

## 刷写

下面是简要步骤。完整流程（含截图和 CHIRP 部分）请见
[karina-v3-k1-install.pdf](karina-v3-k1-install.pdf)。

1. **先备份。** 趁对讲机仍在运行当前固件时，读出并保存它的校准数据和配置。校准数据保存着
   你这台对讲机自己的发射功率和电池参数 —— 丢失它会损失通联距离和读数准确性。
2. **进入刷机模式。** 关闭对讲机，按住 **PTT**，然后开机。
3. 用下列任意一款工具**刷写**对应你机型的文件。
4. **清除内存。** 关闭对讲机，然后按住 **PTT + EXIT** 约两秒钟再开机。
5. **写回校准数据**，然后写入本次发布中的 Karina 校准数据。
6. **复位对讲机**：`MENU` → `RESET` → `VFO`。

| 工具 | 平台 | 文件 |
| --- | --- | --- |
| [UV Studio](https://armel.github.io/uvstudio/#flash) | 网页版（Chrome、Edge、Opera、Brave） | 见工具内说明 |
| [泉盛官方升级软件](https://en.qsfj.com/support/downloads/8483) | Windows | `*.packed.bin` |
| [k5prog](https://github.com/sq5bpf/k5prog) —— `./k5prog -F -YYY -b <file>.bin` | Linux、macOS | `*.bin` |
| [uvtools](https://egzumer.github.io/uvtools) | 网页版（Chrome、Edge） | 见工具内说明 |
| [K5K1 Prog](https://github.com/ERuban/k5k1prog-mac) | macOS | `*.bin` 或 `*.packed.bin` |

开始之前请确认你使用的工具支持你的对讲机。刷机风险由你自己承担。

## 信道与 CHIRP

信道使用带 Karina 驱动模块的 [CHIRP](https://chirpmyradio.com/) 编辑，也可以使用任何能识别
相同信道格式的工具。来自**其他**固件的配置文件不兼容：只有从早期 Karina 版本保存下来的
配置才能写回。

## 文档

| 文档 | 俄文 | 英文 |
| --- | --- | --- |
| 安装与 CHIRP | [karina-v3-k1-install.pdf](karina-v3-k1-install.pdf) | [karina-v3-k1-install-en.pdf](karina-v3-k1-install-en.pdf) |
| 固件使用手册 | [karina-v3-k1-manual.pdf](karina-v3-k1-manual.pdf) | [karina-v3-k1-manual-en.pdf](karina-v3-k1-manual-en.pdf) |

有问题或需要反馈，请到 [Telegram 交流群](https://t.me/k5fwmod)的评论区提出。

## 致谢

Karina 建立在这些把这台对讲机研究透彻的人的成果之上：

- [Dual Tachyon](https://github.com/DualTachyon) —— 最初的开源固件
- [Mikhail (fagci)](https://github.com/fagci) —— Karina 所基于的 mod
- [OneOfEleven](https://github.com/OneOfEleven)、[muzkr](https://github.com/muzkr)、
  [armel](https://github.com/armel)、[Andrej](https://github.com/Tunas1337) —— 固件开发与工具
- [ERuban](https://github.com/ERuban) (@vkusni) —— macOS 版 [K5K1 Prog](https://github.com/ERuban/k5k1prog-mac)
- 文档与测试：DmitroBuka (@DmitrBukatov)、Kolyan (@Kolyanuch)、PunkTracker、
  Avers (@aversreg)、Киловольт Киловольтович、Ivan (@s_ivan96)、Руслан Румянцев
- QUANSHENG，以及所有提供过帮助的人

## 许可证

```
Copyright 2023 Dual Tachyon <https://github.com/DualTachyon>
Copyright 2023 fagci <https://github.com/fagci>
Copyright 2023 OneOfEleven <https://github.com/OneOfEleven>
Copyright 2025 muzkr <https://github.com/muzkr>
Copyright 2025 armel <https://github.com/armel>
Modifications Copyright 2026 autumn1rain <https://github.com/autumn1rain>
```

本项目采用 Apache License 2.0 许可证。完整文本和版权持有者名单见 [LICENSE](LICENSE)。
