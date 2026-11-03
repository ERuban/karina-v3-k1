"""Build the Karina firmware website into docs/ (GitHub Pages).

Usage: python3 scripts/build_site.py

All page texts live in TEXTS below, one block per language. English is the source; any key
a translation leaves out falls back to English, so a half-finished language still builds.
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")

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

TEXTS = {
    "en": {'title': 'Karina firmware for Quansheng UV-K5 V3 and UV-K1',
     'description': 'Karina (autumn rain) firmware for the Quansheng UV-K5 V3, UV-K1 and UV-K1(8): '
                    'spectrum analyser, FM radio, scan lists. Free download.',
     'tagline': 'Community firmware for the Quansheng UV-K5 (V3), UV-K1 and UV-K1(8)',
     'lede': 'Karina adds a spectrum analyser, FM broadcast radio, flexible scanning and a '
             'reworked menu to the radio you already own. Free, open licence, no accounts.',
     'download': 'Download',
     'version_note': 'Latest release on GitHub',
     'source': 'Source code',
     'chat': 'Telegram chat',
     'warning_h': 'Before you flash anything',
     'warning': 'Firmware built for one hardware version bricks another one. Check which radio you '
                'have, and back up your calibration first — it is unique to your radio and nobody '
                'can give it back to you.',
     'radios_h': 'Which radio do I have?',
     'radios_lede': 'Switch the radio off, hold PTT and switch it on: the display shows the '
                    'bootloader version. Its first digit tells you the hardware version.',
     'radios_cols': ['Bootloader starts with', 'Radio', 'Karina build'],
     'radios_rows': [['2, 3, 4, 5', 'UV-K5 V1', 'karina-v1 (separate repository)'],
                     ['1', 'UV-K5 V2', 'not supported'],
                     ['7', 'UV-K5 V3, UV-K1, UV-K1(8)', 'this repository']],
     'radios_note': 'V1 radios carry no marking; V2 and V3 usually have one on the sticker under '
                    'the battery.',
     'v1_note': 'Got the older UV-K5 V1? It has a build of its own, in a separate repository:',
     'features_h': 'What Karina adds',
     'features': [('Spectrum analyser',
                   'Band presets, a free-entry mode, live capture of the active frequency, a '
                   'blacklist for noisy channels, and controls for attenuator, AGC and squelch.'),
                  ('Scanning that behaves',
                   'Scan lists, priority channels checked during the scan, and any channel skipped '
                   'on the fly by switching its attenuator on.'),
                  ('Subtone scan',
                   'Scan CTCSS/DCS tones on the current frequency and store the one that was found '
                   'as the transmit subtone.'),
                  ('FM broadcast radio',
                   'Station search with memories, resumed automatically five seconds after a '
                   'signal on the working channel disappears.'),
                  ('Attenuator in three steps',
                   'ATT1, ATT2 and ATT3 per frequency or channel — useful next to a strong '
                   'transmitter and for skipping channels while scanning.'),
                  ('Power, battery and extras',
                   'HIGH / MID / LOW TX power, a reworked battery saver, dynamic volume, a '
                   'frequency and power randomizer, NOAA, AM and USB modulation.')],
     'install_h': 'Install',
     'install_lede': 'The short version. The full procedure with screenshots is in the '
                     'installation guide below.',
     'install': ['Back up your calibration and configuration while the radio still runs its '
                 'current firmware.',
                 'Switch the radio off, hold <b>PTT</b> and switch it on — that is flash mode.',
                 'Flash the file for your radio with any of the tools below.',
                 'Clear the memory: switch off, then switch on holding <b>PTT + EXIT</b> for about '
                 'two seconds.',
                 'Write your calibration back, then write the Karina calibration from the release.',
                 'Reset the radio: <b>MENU → RESET → VFO</b>.'],
     'tools_h': 'Flashing tools',
     'tools_cols': ['Tool', 'Platform', 'File'],
     'tools_rows': [['UV Studio', 'web (Chrome, Edge, Opera, Brave)', 'see the tool'],
                    ['Official Quansheng updater', 'Windows', '*.packed.bin'],
                    ['k5prog', 'Linux, macOS', '*.bin'],
                    ['uvtools', 'web (Chrome, Edge)', 'see the tool'],
                    ['K5K1 Prog', 'macOS', '*.bin or *.packed.bin']],
     'tools_note': 'Check that your tool supports your radio before you start. You do this at your '
                   'own risk.',
     'docs_h': 'Documentation',
     'docs_lede': 'The installation guide covers flashing and CHIRP; the manual describes every '
                  'menu item and key.',
     'docs_install': 'Installation guide and CHIRP',
     'docs_manual': 'Firmware manual',
     'docs_ru': 'Russian (original)',
     'docs_en': 'English',
     'faq_h': 'Questions',
     'faq': [('Can I flash this into a UV-K5 V1?',
              'No. V1 has a different processor and a different bootloader; the wrong firmware '
              'bricks the radio. V1 owners need the karina-v1 build.'),
             ('Do I really need the calibration backup?',
              "Yes. Calibration holds your own radio's TX power and battery data. It is not in any "
              'release and nobody can restore it for you.'),
             ('Can I keep my settings from another firmware?',
              'No. Only a configuration saved from an earlier Karina version can be written back. '
              'Channels can be moved with CHIRP.'),
             ('The radio asks for a code after I wrote settings from CHIRP.',
              'That happens when a side key is left as NONE. Fill in all four side-key assignments '
              '(short and long press for both keys) before writing.'),
             ('Where do I ask for help?',
              'In the Telegram chat, in the comments. Please say which radio and which firmware '
              'version you have.')],
     'footer_base': "Karina is based on fagci's UV-K5 mod (v1.2.1) and the open firmware work of "
                    'Dual Tachyon, OneOfEleven, muzkr, armel and others.',
     'footer_license': 'Licensed under the Apache License 2.0.',
     'footer_lang': 'Language',
     'translation_note': 'Translated from English. The English page is the authoritative version.',
     'anchor': 'Link to this section'},
    "ru": {'title': 'Прошивка Karina для Quansheng UV-K5 V3 и UV-K1',
     'description': 'Прошивка Karina (autumn rain) для Quansheng UV-K5 V3, UV-K1 и UV-K1(8): '
                    'анализатор спектра, FM-радио, сканлисты. Бесплатно.',
     'tagline': 'Прошивка от сообщества для Quansheng UV-K5 (V3), UV-K1 и UV-K1(8)',
     'lede': 'Karina добавляет анализатор спектра, приём FM-радиовещания, гибкое сканирование и '
             'переработанное меню в рацию, которая у вас уже есть. Бесплатно, открытая лицензия, '
             'без аккаунтов.',
     'download': 'Скачать',
     'version_note': 'Последний релиз на GitHub',
     'source': 'Исходный код',
     'chat': 'Чат в Telegram',
     'warning_h': 'Прежде чем что-то прошивать',
     'warning': 'Прошивка, собранная под одну аппаратную версию, превращает другую в кирпич. '
                'Проверьте, какая у вас рация, и сначала сохраните резервную копию калибровки — '
                'она уникальна для вашей рации, и никто не вернёт её вам.',
     'radios_h': 'Какая у меня рация?',
     'radios_lede': 'Выключите рацию, зажмите PTT и включите её: на экране появится версия '
                    'загрузчика. Её первая цифра указывает аппаратную версию.',
     'radios_cols': ['Загрузчик начинается с', 'Рация', 'Сборка Karina'],
     'radios_rows': [['2, 3, 4, 5', 'UV-K5 V1', 'karina-v1 (отдельный репозиторий)'],
                     ['1', 'UV-K5 V2', 'не поддерживается'],
                     ['7', 'UV-K5 V3, UV-K1, UV-K1(8)', 'этот репозиторий']],
     'radios_note': 'На рациях V1 маркировки нет; у V2 и V3 она обычно есть на наклейке под '
                    'аккумулятором.',
     'features_h': 'Что добавляет Karina',
     'features': [['Анализатор спектра',
                   'Пресеты диапазонов, режим свободного ввода, живой захват активной частоты, '
                   'чёрный список для шумных каналов и управление аттенюатором, АРУ и '
                   'шумоподавителем.'],
                  ['Сканирование, которое работает как надо',
                   'Сканлисты, приоритетные каналы, проверяемые во время сканирования, и пропуск '
                   'любого канала на лету — простым включением его аттенюатора.'],
                  ['Сканирование субтонов',
                   'Сканирование тонов CTCSS/DCS на текущей частоте с сохранением найденного тона '
                   'как субтона передачи.'],
                  ['FM-радиовещание',
                   'Поиск станций с памятью, который автоматически возобновляется через пять '
                   'секунд после пропадания сигнала на рабочем канале.'],
                  ['Аттенюатор в три ступени',
                   'ATT1, ATT2 и ATT3 для каждой частоты или канала — полезно рядом с мощным '
                   'передатчиком и для пропуска каналов при сканировании.'],
                  ['Мощность, батарея и дополнения',
                   'Мощность передачи HIGH / MID / LOW, переработанный экономайзер батареи, '
                   'динамическая громкость, рандомизатор частоты и мощности, NOAA, модуляции AM и '
                   'USB.']],
     'install_h': 'Установка',
     'install_lede': 'Коротко. Полная процедура со скриншотами — в руководстве по установке ниже.',
     'install': ['Сохраните резервную копию калибровки и конфигурации, пока рация ещё работает на '
                 'текущей прошивке.',
                 'Выключите рацию, зажмите <b>PTT</b> и включите её — это режим прошивки.',
                 'Прошейте файл для вашей рации любым из инструментов ниже.',
                 'Очистите память: выключите рацию, затем включите её, удерживая <b>PTT + EXIT</b> '
                 'около двух секунд.',
                 'Запишите обратно свою калибровку, а затем калибровку Karina из релиза.',
                 'Сбросьте рацию: <b>MENU → RESET → VFO</b>.'],
     'tools_h': 'Инструменты для прошивки',
     'tools_cols': ['Инструмент', 'Платформа', 'Файл'],
     'tools_rows': [['UV Studio', 'web (Chrome, Edge, Opera, Brave)', 'см. в инструменте'],
                    ['Официальный апдейтер Quansheng', 'Windows', '*.packed.bin'],
                    ['k5prog', 'Linux, macOS', '*.bin'],
                    ['uvtools', 'web (Chrome, Edge)', 'см. в инструменте'],
                    ['K5K1 Prog', 'macOS', '*.bin или *.packed.bin']],
     'tools_note': 'Перед началом убедитесь, что выбранный инструмент поддерживает вашу рацию. Вы '
                   'делаете это на свой страх и риск.',
     'docs_h': 'Документация',
     'docs_lede': 'Руководство по установке описывает прошивку и CHIRP; руководство по прошивке — '
                  'каждый пункт меню и каждую клавишу.',
     'docs_install': 'Руководство по установке и CHIRP',
     'docs_manual': 'Руководство по прошивке',
     'docs_ru': 'Русский (оригинал)',
     'docs_en': 'Английский',
     'faq_h': 'Вопросы',
     'faq': [['Можно ли прошить это в UV-K5 V1?',
              'Нет. У V1 другой процессор и другой загрузчик; неподходящая прошивка превращает '
              'рацию в кирпич. Владельцам V1 нужна сборка karina-v1.'],
             ['Мне правда нужна резервная копия калибровки?',
              'Да. В калибровке хранятся данные о мощности передачи и батарее именно вашей рации. '
              'Её нет ни в одном релизе, и никто не восстановит её за вас.'],
             ['Можно ли сохранить настройки от другой прошивки?',
              'Нет. Записать обратно можно только конфигурацию, сохранённую из более ранней версии '
              'Karina. Каналы можно перенести через CHIRP.'],
             ['Рация просит код после того, как я записал настройки из CHIRP.',
              'Так бывает, когда боковая клавиша осталась в значении NONE. Перед записью заполните '
              'все четыре назначения боковых клавиш (короткое и длинное нажатие для обеих).'],
             ['Где спросить помощи?',
              'В чате Telegram, в комментариях. Пожалуйста, укажите, какая у вас рация и какая '
              'версия прошивки.']],
     'footer_base': 'Karina основана на моде UV-K5 от fagci (v1.2.1) и на работе над открытыми '
                    'прошивками Dual Tachyon, OneOfEleven, muzkr, armel и других.',
     'footer_license': 'Распространяется по лицензии Apache License 2.0.',
     'footer_lang': 'Язык',
     'translation_note': 'Переведено с английского. Английская версия страницы — основная и имеет '
                         'приоритет.',
     'anchor': 'Ссылка на этот раздел',
     'v1_note': 'Если у вас старая UV-K5 V1 — для неё есть своя сборка, в отдельном репозитории:'},
    "es": {'title': 'Firmware Karina para Quansheng UV-K5 V3 y UV-K1',
     'description': 'Firmware Karina (autumn rain) para Quansheng UV-K5 V3, UV-K1 y UV-K1(8): '
                    'analizador de espectro, radio FM, listas de escaneo. Descarga gratuita.',
     'tagline': 'Firmware comunitario para Quansheng UV-K5 (V3), UV-K1 y UV-K1(8)',
     'lede': 'Karina añade un analizador de espectro, radio FM comercial, escaneo flexible y un '
             'menú rediseñado a la radio que ya tienes. Gratis, licencia abierta, sin cuentas.',
     'download': 'Descargar',
     'version_note': 'Última versión publicada en GitHub',
     'source': 'Código fuente',
     'chat': 'Chat de Telegram',
     'warning_h': 'Antes de flashear nada',
     'warning': 'Un firmware compilado para una versión de hardware inutiliza la otra. Comprueba '
                'qué radio tienes y haz primero una copia de seguridad de tu calibración: es única '
                'de tu radio y nadie puede devolvértela.',
     'radios_h': '¿Qué radio tengo?',
     'radios_lede': 'Apaga la radio, mantén pulsado PTT y enciéndela: la pantalla muestra la '
                    'versión del bootloader. Su primer dígito indica la versión de hardware.',
     'radios_cols': ['El bootloader empieza por', 'Radio', 'Compilación de Karina'],
     'radios_rows': [['2, 3, 4, 5', 'UV-K5 V1', 'karina-v1 (repositorio aparte)'],
                     ['1', 'UV-K5 V2', 'no compatible'],
                     ['7', 'UV-K5 V3, UV-K1, UV-K1(8)', 'este repositorio']],
     'radios_note': 'Las radios V1 no llevan ninguna marca; las V2 y V3 suelen tenerla en la '
                    'pegatina que hay debajo de la batería.',
     'features_h': 'Qué añade Karina',
     'features': [['Analizador de espectro',
                   'Preajustes de banda, un modo de entrada libre, captura en directo de la '
                   'frecuencia activa, una lista negra para canales ruidosos y controles de '
                   'atenuador, AGC y squelch.'],
                  ['Escaneo que se porta bien',
                   'Listas de escaneo, canales prioritarios comprobados durante el escaneo y '
                   'cualquier canal omitido sobre la marcha con solo activar su atenuador.'],
                  ['Escaneo de subtonos',
                   'Escanea los subtonos CTCSS/DCS de la frecuencia actual y guarda el que se haya '
                   'encontrado como subtono de transmisión.'],
                  ['Radio FM comercial',
                   'Búsqueda de emisoras con memorias, que se reanuda automáticamente cinco '
                   'segundos después de que desaparezca la señal del canal de trabajo.'],
                  ['Atenuador en tres pasos',
                   'ATT1, ATT2 y ATT3 por frecuencia o por canal: útil cerca de un transmisor '
                   'potente y para saltarse canales durante el escaneo.'],
                  ['Potencia, batería y extras',
                   'Potencia de transmisión HIGH / MID / LOW, ahorro de batería rediseñado, '
                   'volumen dinámico, aleatorizador de frecuencia y potencia, NOAA, AM y '
                   'modulación USB.']],
     'install_h': 'Instalación',
     'install_lede': 'La versión corta. El procedimiento completo con capturas de pantalla está en '
                     'la guía de instalación que encontrarás más abajo.',
     'install': ['Haz una copia de seguridad de tu calibración y de tu configuración mientras la '
                 'radio todavía ejecuta su firmware actual.',
                 'Apaga la radio, mantén pulsado <b>PTT</b> y enciéndela: ese es el modo de '
                 'flasheo.',
                 'Flashea el archivo correspondiente a tu radio con cualquiera de las herramientas '
                 'de abajo.',
                 'Borra la memoria: apaga la radio y vuelve a encenderla manteniendo pulsado '
                 '<b>PTT + EXIT</b> durante unos dos segundos.',
                 'Vuelve a escribir tu calibración y, después, escribe la calibración de Karina '
                 'incluida en la versión publicada.',
                 'Reinicia la radio: <b>MENU → RESET → VFO</b>.'],
     'tools_h': 'Herramientas de flasheo',
     'tools_cols': ['Herramienta', 'Plataforma', 'Archivo'],
     'tools_rows': [['UV Studio', 'web (Chrome, Edge, Opera, Brave)', 'consulta la herramienta'],
                    ['Actualizador oficial de Quansheng', 'Windows', '*.packed.bin'],
                    ['k5prog', 'Linux, macOS', '*.bin'],
                    ['uvtools', 'web (Chrome, Edge)', 'consulta la herramienta'],
                    ['K5K1 Prog', 'macOS', '*.bin o *.packed.bin']],
     'tools_note': 'Comprueba que tu herramienta sea compatible con tu radio antes de empezar. Lo '
                   'haces bajo tu propia responsabilidad.',
     'docs_h': 'Documentación',
     'docs_lede': 'La guía de instalación cubre el flasheo y CHIRP; el manual describe cada opción '
                  'del menú y cada tecla.',
     'docs_install': 'Guía de instalación y CHIRP',
     'docs_manual': 'Manual del firmware',
     'docs_ru': 'Ruso (original)',
     'docs_en': 'Inglés',
     'faq_h': 'Preguntas',
     'faq': [['¿Puedo flashear esto en una UV-K5 V1?',
              'No. La V1 tiene un procesador y un bootloader distintos; el firmware equivocado '
              'inutiliza la radio. Quien tenga una V1 necesita la compilación karina-v1.'],
             ['¿De verdad necesito la copia de la calibración?',
              'Sí. La calibración guarda los datos de potencia de transmisión y de batería propios '
              'de tu radio. No está en ninguna versión publicada y nadie puede restaurártela.'],
             ['¿Puedo conservar mis ajustes de otro firmware?',
              'No. Solo se puede volver a escribir una configuración guardada desde una versión '
              'anterior de Karina. Los canales se pueden trasladar con CHIRP.'],
             ['La radio me pide un código después de escribir los ajustes desde CHIRP.',
              'Eso ocurre cuando una tecla lateral queda en NONE. Rellena las cuatro asignaciones '
              'de las teclas laterales (pulsación corta y larga de ambas teclas) antes de '
              'escribir.'],
             ['¿Dónde puedo pedir ayuda?',
              'En el chat de Telegram, en los comentarios. Indica, por favor, qué radio y qué '
              'versión del firmware tienes.']],
     'footer_base': 'Karina se basa en el mod UV-K5 de fagci (v1.2.1) y en el trabajo de firmware '
                    'abierto de Dual Tachyon, OneOfEleven, muzkr, armel y otros.',
     'footer_license': 'Distribuido bajo la licencia Apache License 2.0.',
     'footer_lang': 'Idioma',
     'translation_note': 'Traducido del inglés. La página en inglés es la versión autorizada.',
     'anchor': 'Enlace a esta sección',
     'v1_note': '¿Tienes la antigua UV-K5 V1? Tiene su propia versión, en un repositorio aparte:'},
    "de": {'title': 'Karina Firmware für Quansheng UV-K5 V3 und UV-K1',
     'description': 'Karina (autumn rain) Firmware für Quansheng UV-K5 V3, UV-K1 und UV-K1(8): '
                    'Spektrumanalysator, FM-Radio, Suchlisten. Gratis-Download.',
     'tagline': 'Community-Firmware für Quansheng UV-K5 (V3), UV-K1 und UV-K1(8)',
     'lede': 'Karina ergänzt Ihr vorhandenes Funkgerät um einen Spektrumanalysator, '
             'FM-Rundfunkempfang, flexiblen Suchlauf und ein überarbeitetes Menü. Kostenlos, '
             'offene Lizenz, ohne Konten.',
     'download': 'Herunterladen',
     'version_note': 'Neueste Version auf GitHub',
     'source': 'Quellcode',
     'chat': 'Telegram-Chat',
     'warning_h': 'Bevor Sie etwas flashen',
     'warning': 'Firmware, die für eine Hardware-Version gebaut wurde, macht eine andere '
                'unbrauchbar. Prüfen Sie, welches Funkgerät Sie haben, und sichern Sie zuerst Ihre '
                'Kalibrierung — sie ist einmalig für Ihr Gerät und niemand kann sie Ihnen '
                'zurückgeben.',
     'radios_h': 'Welches Funkgerät habe ich?',
     'radios_lede': 'Schalten Sie das Funkgerät aus, halten Sie PTT gedrückt und schalten Sie es '
                    'ein: Das Display zeigt die Bootloader-Version. Deren erste Ziffer nennt Ihnen '
                    'die Hardware-Version.',
     'radios_cols': ['Bootloader beginnt mit', 'Funkgerät', 'Karina-Build'],
     'radios_rows': [['2, 3, 4, 5', 'UV-K5 V1', 'karina-v1 (eigenes Repository)'],
                     ['1', 'UV-K5 V2', 'nicht unterstützt'],
                     ['7', 'UV-K5 V3, UV-K1, UV-K1(8)', 'dieses Repository']],
     'radios_note': 'V1-Geräte tragen keine Kennzeichnung; V2 und V3 haben meist eine auf dem '
                    'Aufkleber unter dem Akku.',
     'features_h': 'Was Karina hinzufügt',
     'features': [['Spektrumanalysator',
                   'Bandvorgaben, freie Frequenzeingabe, Live-Mitschnitt der aktiven Frequenz, '
                   'eine Sperrliste für verrauschte Kanäle sowie Einstellungen für Dämpfungsglied, '
                   'AGC und Rauschsperre.'],
                  ['Suchlauf, der sich benimmt',
                   'Suchlisten, Prioritätskanäle, die während des Suchlaufs geprüft werden, und '
                   'jeder Kanal lässt sich im laufenden Betrieb überspringen, indem Sie sein '
                   'Dämpfungsglied einschalten.'],
                  ['Subton-Suchlauf',
                   'Suchen Sie CTCSS/DCS-Töne auf der aktuellen Frequenz und speichern Sie den '
                   'gefundenen Ton als Sende-Subton.'],
                  ['FM-Rundfunkempfang',
                   'Sendersuche mit Speicherplätzen, die fünf Sekunden nach dem Verschwinden eines '
                   'Signals auf dem Arbeitskanal automatisch fortgesetzt wird.'],
                  ['Dämpfungsglied in drei Stufen',
                   'ATT1, ATT2 und ATT3 je Frequenz oder Kanal — nützlich neben einem starken '
                   'Sender und zum Überspringen von Kanälen während des Suchlaufs.'],
                  ['Sendeleistung, Akku und Extras',
                   'Sendeleistung HIGH / MID / LOW, ein überarbeiteter Akkusparmodus, dynamische '
                   'Lautstärke, ein Frequenz- und Leistungs-Randomizer, NOAA sowie AM- und '
                   'USB-Modulation.']],
     'install_h': 'Installation',
     'install_lede': 'Die Kurzfassung. Das vollständige Verfahren mit Screenshots steht in der '
                     'Installationsanleitung weiter unten.',
     'install': ['Sichern Sie Ihre Kalibrierung und Ihre Konfiguration, solange auf dem Funkgerät '
                 'noch die aktuelle Firmware läuft.',
                 'Schalten Sie das Funkgerät aus, halten Sie <b>PTT</b> gedrückt und schalten Sie '
                 'es ein — das ist der Flash-Modus.',
                 'Flashen Sie die Datei für Ihr Funkgerät mit einem der unten genannten Werkzeuge.',
                 'Löschen Sie den Speicher: ausschalten, dann mit gedrückter Taste <b>PTT + '
                 'EXIT</b> etwa zwei Sekunden lang einschalten.',
                 'Schreiben Sie Ihre Kalibrierung zurück und danach die Karina-Kalibrierung aus '
                 'dem Release.',
                 'Setzen Sie das Funkgerät zurück: <b>MENU → RESET → VFO</b>.'],
     'tools_h': 'Flash-Werkzeuge',
     'tools_cols': ['Werkzeug', 'Plattform', 'Datei'],
     'tools_rows': [['UV Studio', 'web (Chrome, Edge, Opera, Brave)', 'siehe Werkzeug'],
                    ['Offizielles Quansheng-Update-Programm', 'Windows', '*.packed.bin'],
                    ['k5prog', 'Linux, macOS', '*.bin'],
                    ['uvtools', 'web (Chrome, Edge)', 'siehe Werkzeug'],
                    ['K5K1 Prog', 'macOS', '*.bin oder *.packed.bin']],
     'tools_note': 'Prüfen Sie vor dem Start, ob Ihr Werkzeug Ihr Funkgerät unterstützt. Sie tun '
                   'dies auf eigene Gefahr.',
     'docs_h': 'Dokumentation',
     'docs_lede': 'Die Installationsanleitung behandelt das Flashen und CHIRP; das Handbuch '
                  'beschreibt jeden Menüpunkt und jede Taste.',
     'docs_install': 'Installationsanleitung und CHIRP',
     'docs_manual': 'Firmware-Handbuch',
     'docs_ru': 'Russisch (Original)',
     'docs_en': 'Englisch',
     'faq_h': 'Fragen',
     'faq': [['Kann ich das in ein UV-K5 V1 flashen?',
              'Nein. Das V1 hat einen anderen Prozessor und einen anderen Bootloader; die falsche '
              'Firmware macht das Funkgerät unbrauchbar. Besitzer eines V1 brauchen den Build '
              'karina-v1.'],
             ['Brauche ich die Sicherung der Kalibrierung wirklich?',
              'Ja. Die Kalibrierung enthält die Sendeleistungs- und Akkudaten Ihres eigenen '
              'Funkgeräts. Sie liegt keinem Release bei und niemand kann sie für Sie '
              'wiederherstellen.'],
             ['Kann ich meine Einstellungen aus einer anderen Firmware behalten?',
              'Nein. Nur eine Konfiguration, die aus einer früheren Karina-Version gesichert '
              'wurde, lässt sich zurückschreiben. Kanäle können Sie mit CHIRP übernehmen.'],
             ['Das Funkgerät fragt nach einem Code, nachdem ich Einstellungen aus CHIRP '
              'geschrieben habe.',
              'Das passiert, wenn eine Seitentaste auf NONE steht. Belegen Sie vor dem Schreiben '
              'alle vier Seitentasten-Funktionen (kurzer und langer Druck für beide Tasten).'],
             ['Wo bekomme ich Hilfe?',
              'Im Telegram-Chat, in den Kommentaren. Bitte nennen Sie dabei Ihr Funkgerät und Ihre '
              'Firmware-Version.']],
     'footer_base': 'Karina basiert auf dem UV-K5-Mod von fagci (v1.2.1) und der offenen '
                    'Firmware-Arbeit von Dual Tachyon, OneOfEleven, muzkr, armel und anderen.',
     'footer_license': 'Lizenziert unter der Apache-Lizenz 2.0.',
     'footer_lang': 'Sprache',
     'translation_note': 'Aus dem Englischen übersetzt. Die englische Seite ist die maßgebliche '
                         'Fassung.',
     'anchor': 'Link zu diesem Abschnitt',
     'v1_note': 'Sie haben noch ein UV-K5 V1? Dafür gibt es eine eigene Firmware in einem '
                'separaten Repository:'},
    "zh": {'title': 'Karina 固件：Quansheng UV-K5 V3 和 UV-K1',
     'description': '适用于 Quansheng UV-K5 V3、UV-K1 和 UV-K1(8) 的 Karina（autumn '
                    'rain）固件：频谱分析仪、调频广播、扫描列表。免费下载。',
     'tagline': '面向 Quansheng UV-K5（V3）、UV-K1 和 UV-K1(8) 的社区固件',
     'lede': 'Karina 为你手中的对讲机增加了频谱分析仪、调频广播、灵活的扫描功能和重新设计的菜单。免费、开放授权、无需注册账号。',
     'download': '下载',
     'version_note': 'GitHub 上的最新发布版本',
     'source': '源代码',
     'chat': 'Telegram 聊天群',
     'warning_h': '刷写之前请注意',
     'warning': '为某个硬件版本编译的固件会把另一个版本刷成砖。请先确认你手上是哪款对讲机，并先备份校准数据——它是你这台对讲机独有的，没有人能把它还给你。',
     'radios_h': '我的对讲机是哪一款？',
     'radios_lede': '关闭对讲机，按住 PTT 再开机：屏幕会显示 Bootloader（引导程序）版本号。它的第一位数字就代表硬件版本。',
     'radios_cols': ['Bootloader 开头数字', '对讲机', 'Karina 版本'],
     'radios_rows': [['2、3、4、5', 'UV-K5 V1', 'karina-v1（独立仓库）'],
                     ['1', 'UV-K5 V2', '不支持'],
                     ['7', 'UV-K5 V3、UV-K1、UV-K1(8)', '本仓库']],
     'radios_note': 'V1 机型没有任何标识；V2 和 V3 通常在电池下方的标签上有标注。',
     'features_h': 'Karina 新增的功能',
     'features': [['频谱分析仪', '内置波段预设和自由输入模式，可实时捕获当前有信号的频率，支持噪声频道黑名单，并可调节衰减器、AGC 和静噪。'],
                  ['更听话的扫描', '支持扫描列表、扫描过程中检查优先频道，还可以打开某个频道的衰减器，在扫描中随时跳过它。'],
                  ['亚音扫描', '在当前频率上扫描 CTCSS/DCS 亚音，并把扫到的亚音保存为发射亚音。'],
                  ['调频广播', '支持电台搜索和记忆，工作频道上的信号消失五秒后自动恢复收听。'],
                  ['三级衰减器', '可按频率或频道设置 ATT1、ATT2 和 ATT3——在大功率发射台旁边很有用，也可用于扫描时跳过频道。'],
                  ['功率、电池及其他',
                   'HIGH / MID / LOW 三挡发射功率、重新设计的省电模式、动态音量、频率与功率随机化、NOAA、AM 和 USB 调制。']],
     'install_h': '安装',
     'install_lede': '这里是简要步骤。带截图的完整流程见下方的安装指南。',
     'install': ['趁对讲机还运行着当前固件，先备份你的校准数据和配置。',
                 '关闭对讲机，按住 <b>PTT</b> 再开机——这就是刷写模式。',
                 '用下面任意一个工具刷入适合你对讲机的文件。',
                 '清除内存：先关机，然后按住 <b>PTT + EXIT</b> 约两秒再开机。',
                 '先把你自己的校准数据写回去，然后写入发布包中的 Karina 校准数据。',
                 '复位对讲机：<b>MENU → RESET → VFO</b>。'],
     'tools_h': '刷写工具',
     'tools_cols': ['工具', '平台', '文件'],
     'tools_rows': [['UV Studio', 'web（Chrome、Edge、Opera、Brave）', '见工具内说明'],
                    ['Quansheng 官方升级工具', 'Windows', '*.packed.bin'],
                    ['k5prog', 'Linux、macOS', '*.bin'],
                    ['uvtools', 'web（Chrome、Edge）', '见工具内说明'],
                    ['K5K1 Prog', 'macOS', '*.bin 或 *.packed.bin']],
     'tools_note': '开始之前请确认你用的工具支持你的对讲机。操作风险由你自行承担。',
     'docs_h': '文档',
     'docs_lede': '安装指南介绍刷写和 CHIRP；使用手册逐项说明每个菜单项和按键。',
     'docs_install': '安装指南与 CHIRP',
     'docs_manual': '固件使用手册',
     'docs_ru': '俄语（原版）',
     'docs_en': '英语',
     'faq_h': '常见问题',
     'faq': [['可以把它刷进 UV-K5 V1 吗？',
              '不可以。V1 使用不同的处理器和不同的 Bootloader（引导程序），刷错固件会把对讲机变成砖。V1 用户需要使用 karina-v1 版本。'],
             ['我真的必须备份校准数据吗？', '是的。校准数据保存着你这台对讲机自己的发射功率和电池参数。它不包含在任何发布包里，也没有人能替你恢复。'],
             ['可以保留我在其他固件上的设置吗？', '不可以。只有从早期 Karina 版本保存下来的配置才能写回。频道可以用 CHIRP 迁移。'],
             ['用 CHIRP 写入设置后，对讲机要求输入密码。', '这是因为某个侧键被留成了 NONE。写入前请把四个侧键功能全部填好（两个按键的短按和长按）。'],
             ['我可以去哪里求助？', '到 Telegram 聊天群的评论区提问。请说明你用的是哪款对讲机、哪个固件版本。']],
     'footer_base': 'Karina 基于 fagci 的 UV-K5 mod（v1.2.1），以及 Dual Tachyon、OneOfEleven、muzkr、armel '
                    '等人的开源固件成果。',
     'footer_license': '采用 Apache License 2.0 授权。',
     'footer_lang': '语言',
     'translation_note': '本页译自英文版。英文页面为权威版本。',
     'anchor': '链接到本节',
     'v1_note': '还在用较早的 UV-K5 V1？它有自己的固件，放在另一个仓库里：'},
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
    """English is the source; a language only needs the keys it actually translates."""
    t = dict(TEXTS["en"])
    t.update({k: v for k, v in TEXTS.get(lang, {}).items() if v})
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
