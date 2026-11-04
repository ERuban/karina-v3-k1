**Also, kaputt gemacht?**
**Höchste Zeit, die Anleitung aufzuschlagen.**

*Karina (autumn rain) — QUANSHENG UV-K5 (V3), UV-K1, UV-K1(8)*

![screenshot](images/p01_2.png)
![screenshot](images/p01_1.png)
![screenshot](images/p01_3.png)

## Firmware KARINA (autumn rain) — Beschreibung

**Version 21.08.2026**

**(Versionsnummer = Tag.Monat der Veröffentlichung)**
==**Ergänzungen, Präzisierungen und neue Funktionen sind farbig markiert**==

 **!!! SICHERN SIE IHRE WERKSKALIBRIERUNGSDATEN !!!**
**nach dem Flashen muss die Kalibrierung aktualisiert werden**

**und anschließend muss ein Reset durchgeführt werden: menu -> reset -> vfo**

## INHALT:

**1. HAUPTBILDSCHIRM**

**2. MENÜ**
2.1. Navigation im Menü
2.2. Arbeits-Frequenzbänder (BANDS)
==2.3. Hauptmenü==
==2.4. Verstecktes Menü==

**3. TASTENFUNKTIONEN**
==3.1. Service-Tastenkombinationen.==
==3.2 Fronttasten==
3.3. Seitentasten
3.4. Eingabe einer Frequenz auf dem Hauptbildschirm
==3.5. Suchlauf in den Modi VFO und MR==

**4. SPEKTRUMANALYSATOR**
4.1. Grundlegender Spektrum-Modus
4.2. Zusätzliche Funktionstasten im Modus des Spektrumanalysators
4.3. Einstellungen des Spektrumanalysators
4.3.1. Arbeiten im Modus „freie Eingabe“
4.3.2. Bearbeiten der Presets
4.3.3. Einstellen der zusätzlichen Parameter des Spektrumanalysators
4.4. Modus der aktiven Frequenzerfassung — „Detailansicht“
4.5. Register des Modus der aktiven Frequenzerfassung
4.6. Tastenbelegung in den Modi des Spektrumanalysators

==**5. HÄUFIG GESTELLTE FRAGEN, MÖGLICHE PROBLEME**==
==**UND IHRE LÖSUNG.**==

## 1. HAUPTBILDSCHIRM.

![screenshot](images/p03_1.png)

![screenshot](images/p03_2.png)

**1.**
Statuszeile / folgende Symbole können angezeigt werden:

**S** – Akkusparmodus ist eingeschaltet – siehe Abschnitt 2, Punkt 14;
**L** – Tastatur ist gesperrt (Lock) – siehe Abschnitt 3, Punkt F (langes F);
**F** - Umschaltung in den Optionsmodus – siehe Abschnitt 3, Punkt F (kurzes F);
**DW** – Dual-Watch-Modus – siehe Abschnitt 2, Punkt 17;
**A** - automatische Einstellung des Subtons des letzten Empfangs – siehe Abschnitt 3, Punkt 0 (F + sehr langes 0);
**D** - dynamische Lautstärke – siehe Abschnitt 3, Punkt 9 (langes 9);
**r** - Zufallsgenerator für Frequenz und Sendeleistung – siehe Abschnitt 3, Punkt 8 (F + sehr langes 8);
**RXTX** – automatische Bake – siehe Abschnitt 3, Punkte 1, 2, 3;
**x** - Frequenzerfassung im Hintergrund – siehe Abschnitt 3, Punkt 1 (langes 1);
*Während ein Signal mit Subton empfangen wird, zeigt die Statuszeile den*
*analogen CTCSS-Ton (als Zahl) oder den digitalen DCS-Code (in der Form D125) an*

**2.**
Empfängerauswahl / Aktivität / VFO/MR-Modus
**3.**
Anzeige des letzten Empfangs / Frequenzablage des letzten Empfangs (x10 Hz)
**4.**
Kanalparameter / folgende Symbole können angezeigt werden:

**ATT 1, ATT 2** - Dämpfungsglied eingeschaltet (schnell ein / ändern / aus - `*` )
**DCS, CT** - Typ des eingestellten Subtons – siehe Abschnitt 2, Punkt 4;
**HIGH, MID, LOW** – aktuelle Sendeleistung (schnelles Umschalten – langes 6)
**R** - Reverse-Modus eingeschaltet – (langes 8);
**12,5k, 25k** - Kanalbandbreite – (schnelles Umschalten F+7)
**SCR** - analoger Scrambler (2.3. Hauptmenü, Punkt 11)
**5.**
S-Meter-Skala
**6.**
Empfängerauswahl / Aktivität / VFO/MR-Modus
**7.**
Empfang – RX / Senden - TX

**8.**
Anzeige des Akkuladezustands
**9.**
Name des Speicherkanals / Frequenz
**10.**
Zugewiesene Suchliste (- erste, - zweite)
 - der Kanal ist in beiden Suchlisten
 - der Kanal ist in keiner Suchliste
**11.**
Signalpegel des S-Meters
**12.**
Modulationsart - AM/FM/SSB (Umschaltung mit langem 7)

## 2. MENÜ.

### 2.1. Navigation im Menü.

**Verwenden Sie die Pfeiltasten** ▲ **/** ▼ **oder geben Sie die Nummer des Punktes direkt über die Tastatur ein (01 oder 22…)**
***Achtung!!!*** *Die Menüpunkte 2, 3, 4, 5, 6, 7, 8, 9, 10, 26 und 39 werden*
*individuell für die Bänder A und B sowie für jedes Frequenzband (Band) eingestellt.*

### 2.2. Arbeits-Frequenzbänder (Bands):

1.00000 – 108.99990 MHz; 109.00000 – 139.99990 MHz; 140.00000 – 199.99990 MHz
200.00000 – 279.99990 MHz; 280.00000 – 399.99990 MHz; 400.00000 – 669.99990 MHz
700.00000 – 3200.99990 MHz.
Die Genauigkeit des Frequenzwertes hängt von dem in Punkt 2 (Step) eingestellten Schritt ab.

### 2.3. Hauptmenü.

**1.**
**Sql** – Empfindlichkeitsstufe der Rauschsperre, wird gleichzeitig für das obere (**A**) und das untere (**B**) Band eingestellt (siehe auch die Beschreibung von Punkt 35)
**2.**
**Step** – Frequenzschritt. (für CB = 5/10; Satcom, Avia = 5/25; alles Übrige = 6,25/12,5).
**3.**
**Power** – Sendeleistung des Funkgeräts. **High / Middle / Low**.
***4.***
**R_DCS** – digital codierter Subton für den Empfang (Digital-Coded Squelch), *bei eingeschalteter Funktion öffnet die Rauschsperre erst, nachdem dieser Subton empfangen wurde. (gilt nur für FM-Modulation)*
***5.***
**R_CTCS** – analoger Subton für den Empfang (Continuous Tone-Coded Squelch System), *bei eingeschalteter Funktion öffnet die Rauschsperre erst, nachdem dieser Subton empfangen wurde. (gilt nur für FM-Modulation)*
***6.***
**T_DCS** – digital codierter Subton für das Senden, *bei eingeschalteter Funktion sendet das Funkgerät diesen Ton aus. (gilt nur für FM-Modulation)*
***7.***
**T_CTCS** – analoger Subton für das Senden, *bei eingeschalteter Funktion sendet das Funkgerät diesen Ton aus. (gilt nur für FM-Modulation)*
**8.**
**Shift** – Vorzeichen der Sendefrequenzablage (RX/TX-Split) **+**/**–**/**upc.**
*(Upconverter - bei Verwendung eines Downconverters)*
**9.**
**Offs** – Wert der Sendefrequenzablage.
**10. W/N** – die vom Funkgerät verwendete Bandbreite:
- **25 kHz** - Wide
- **12,5 kHz** - Narrow.
**11. Scrambl** – analoger Scrambler
*wandelt das ursprüngliche Sprachsignal um, indem dessen Amplituden-, Frequenz- und Zeitparameter in verschiedenen Kombinationen verändert werden (1-10 – verschleiert die Sprache, 11-20 – verändert die Tonhöhe der Sprache).*

**12. BusyCL** – das Senden auf einem belegten Kanal wird blockiert: während das Funkgerät ein Signal empfängt, löst ein Druck auf PTT keine Aussendung aus.
**13. Mem_ch** – Frequenz und Einstellungen in einem Speicherkanal ablegen
*jede Änderung der Einstellungen des aktiven Kanals (im Kanalmodus (MR)) wird nur dann gespeichert, wenn sie über diesen Menüpunkt bestätigt wird; geschieht dies nicht, kehren die Kanaleinstellungen zu den zuvor gespeicherten zurück, sobald Sie auf einen anderen Kanal wechseln oder das Funkgerät AUS/EIN schalten.*
**14. Save** – Akkusparmodus (Verhältnis zwischen Aktivzeit und Schlafzeit). **MAX** – maximale Energieeinsparung x10
*Die maximale Energieeinsparung wird mit Save=Max zusammen mit DW=OFF erreicht. Die optimale Einstellung ist 1:3. Bei eingeschalteter Funktion erscheint von Zeit zu Zeit das Symbol* ***S*** *in der Statuszeile* ==*(siehe auch die Beschreibung von Punkt 25 Roger (Roger=5)).*==
***15.*** **VOX** – sprachgesteuerte Aussendung (1-10 Mikrofonempfindlichkeit)
*beim Aufrufen des Menüs mit „M“ wird VOX gesperrt, damit es nicht durch Tastendrücke ausgelöst wird.*
**16. Light** – Displaybeleuchtung. Sie wird in 2 Schritten eingestellt: Dauer und Helligkeit:
 **EINSTELLUNG DER BELEUCHTUNGSDAUER:**
**OFF** – vollständige Abdunklung (auch die RX/TX-LEDs bleiben dunkel);
**KEY** – wie OFF, jedoch schaltet sich die Beleuchtung beim Druck auf eine Fronttaste für 5 Sekunden ein**;**
**2, 5, 10, 20 sec**, **2 min** – Beleuchtungsdauer. Die Beleuchtung bleibt für die gewählte Zeit an, erlischt jedoch erst nach dem Ende des Empfangs;
**ON** – Beleuchtung dauerhaft an.
 **EINSTELLUNG DER BELEUCHTUNGSHELLIGKEIT:**
**bri 0-7 –** Einstellung der Beleuchtungshelligkeit.
Stellen Sie dazu zuerst die Beleuchtungsdauer ein, rufen Sie dann den Punkt **Light** erneut auf und stellen Sie die Helligkeit ein.
**17. DW** – Dual-Watch-Modus für die Frequenzen der Bänder A und B:
- **Chan_A / Chan_B** – DW-Funktion einschalten.
- **SCAN** – das aktive Band **A / B** bleibt das Arbeitsband, das andere durchsucht die Kanäle der aktiven Suchliste.
- **OFF** – Dual-Watch-Modus ausschalten.
==**ACHTUNG**: bei eingeschalteter Hintergrunderfassung (langer Druck auf Taste 1) wird DW=ON automatisch aktiviert *(die erfasste Frequenz wird in VFO-B angezeigt).*==
**18. Beep** – Tonsignale beim Einschalten des Funkgeräts, bei schwachem Akku und wenn im Modus der Frequenzerfassung im Hintergrund eine Frequenz gefunden wird (Tastendrücke werden nicht von einem Ton begleitet).
**19. TxTime** – Begrenzung der Dauer einer Dauersendung und des Bakenbetriebs.
**20. Scan** – Art des Anhaltens bzw. Fortsetzens des Suchlaufs (diese Einstellung gilt auch für den Spektrumanalysator):

- **CO** – der Suchlauf wird fortgesetzt, nachdem der Träger verschwunden ist ==(optimal);==

- **TO** – Fortsetzen des Suchlaufs nach einer Pause von 5 Sekunden *(im Spektrum kann ein starkes Signal zeitweise ausfallen / hängen bleiben, der „Freeze-Effekt“);*
- **SE** – der Suchlauf wird vollständig angehalten, sobald ein Signal gefunden wurde. Die Tasten ▲**/**▼ setzen den Suchlauf fort *(*==*bei gewähltem SE*== *werden im Spektrum Frequenzen, die bereits in die „Loot“ übernommen wurden, nicht erneut „gesucht“).*

**21. Name** – Auswahl der Darstellungsart für Kanalnamen (verfügbare Optionen: **NAME** - Name, **CHAN** - Kanal, **FREQ** - Frequenz, **NAME+F** - Name + Frequenz).

**22. STE** – beseitigt das Zischen/Rauschen/„Pfft“ am Ende einer Aussendung. *(Beim Loslassen von PTT wird ein kurzer 55-Hz-Ton ausgesendet, der anderen Funkgeräten mitteilt, dass die Aussendung beendet ist und die Tonwiedergabe stummgeschaltet werden soll.)*

**23. Mic** – Mikrofonempfindlichkeit:

- **0** – schwellenloses empfindliches Mikrofon (am besten mit **tx_filt = 1-2)**;
- **1** – Minimum – (am besten mit **tx_filt = 0-1)**;
- **2** – Mittel (am besten mit **tx_filt = 1)**;
- **3** – angehoben *(besser für Weitverbindungen; auf kurzer Distanz entsteht ein Echo)* (am besten mit **tx_filt = 1)**;
- **4** – angehoben **empfohlen** *(*für eine ruhige Umgebung, am besten mit **tx_filt = 1)**;
- **5** – MAX *(die Umgebungsgeräusche werden hörbar)* (am besten mit **tx_filt = 1)***.*

**24. SList** – Auswahl der Suchliste **1** / **2** / **3** (3 - durchsucht alle Kanäle aus dem Speicher)

*Das Hinzufügen / Entfernen des aktiven Kanals zu bzw. aus den Suchlisten (hinzufügen / entfernen ist nur in SList 1 und 2 möglich) erfolgt mit der Kombination F+1 vom Hauptbildschirm aus; bestätigt wird dies durch das Erscheinen / Verschwinden des Symbols aus Punkt 9 auf S. 2.*

*Solange SList 3 aktiv ist, können keine Kanäle hinzugefügt oder entfernt werden!*

*Zusätzlich können Sie mit F+9 2 Prioritätskanäle für den Suchlauf festlegen; Einzelheiten siehe Abschnitt „TASTENFUNKTIONEN“ (9 CALL).*

**25. Roger** – Tonsignal am Ende einer Aussendung (2 funktionierende Varianten zur Auswahl)

*Die zusätzlichen Roger 3-55 sind Testfunktionen – blättern Sie nicht ohne Grund durch sie:*

*Roger 3 - automatische Frequenzerfassung mit größerer Reichweite (siehe Abschnitt „Tastenfunktionen“);*

*Roger 4 – schaltet das automatische Dämpfungsglied aus (OFF);*

*Roger 5 - Modus mit verbessertem Energiesparen + Beschleunigung von: DW-Umschaltung, Subtonmessung, SQL-Prüfung im Energiesparbetrieb. Ein anderer Arbeitsalgorithmus.*

*Roger 6 – inverse Korrektur der Sendefrequenz durch AFC (zum Ausgleich der Dopplerverschiebung);*

*Roger 7 – direkte Korrektur der Sendefrequenz durch AFC*

*(Automatische Abstimmung der Sendefrequenz durch AFC. Nach dem Empfang eines Signals merkt sich das Funkgerät die Frequenzablage und korrigiert die Aussendung. Die Taste EXIT setzt die Korrektur zurück.)*

*Roger 8 – Software-AGC aus AM_fix in FM.*

**26. Modulat** – Modulationsart **FM / AM / SSB** *(standardmäßig FM, wirkt nur beim Empfang).*

**27. AM_fix** – schaltet die AM-AGC ein, um den Empfang von AM-Signalen zu verbessern *(bei aktiver Funktion werden im Modus „Frequenzerfassung“ im Spektrum die Register nicht angepasst, wenn Amplitudenmodulation eingestellt ist).*

**28. AMf_lvl** – stellt den Pegel der AM-AGC ein *(unter bestimmten Bedingungen verringert es das Rauschen).*

**29. LNA_hi** – schaltet den rauscharmen Vorverstärker ein *(in Umgebungen mit starken Störungen schaltet man ihn besser aus).*

*Bei ausgeschaltetem Vorverstärker ist das Spektrum „flach“; bei eingeschaltetem Vorverstärker „erwacht“ das Spektrum.*

*Die ergänzende Beschreibung des Wertes MAN finden Sie in der Beschreibung der Register des Spektrumanalysator-Modus.*

**30. rx_filt** – verändert die Klangfarbe des empfangenen Signals *(1 - hebt die Tiefen an, 2 und 3 - senken die Tiefen ab und heben die Höhen an (****3 ist optimal****)*

**31. tx_filt** – verändert die Modulation beim Senden (Voreinstellung für das Register Tx3k) *0 – werkseitig, 1 – verringert sie* ***(optimal)****, 2, 3 - erhöhen die Modulation; beim empfangenden Funkgerät können ein Pfeifen oder ein Zerhacken der Rauschsperre auftreten.*

*Treten Probleme auf, setzen Sie die Menüpunkte 30, 31 =* ***1****, starten Sie das Funkgerät neu und setzen Sie sie anschließend =* ***0****)*

**32. Del_ch** – Speicherkanal löschen

**33. Reset** – Konfiguration des Funkgeräts zurücksetzen:

==-== ==**VFO**== – Einstellungen des Funkgeräts und die VFO-Bänder zurücksetzen

==-== ==**ALL**== ==– alle Einstellungen des Funkgeräts zurücksetzen, einschließlich== Löschen der Kanäle

==*(die Kalibrierungen sind davon nicht betroffen).*==

**34. Re-name** – Kanal umbenennen (`*` - nächstes Zeichen) – bei neu gespeicherten Kanälen, für die kein Name vergeben wurde, wird während des Suchlaufs «**,,,,,,,,,»** angezeigt; blättern Sie bei der Namenseingabe mit `*` über die leeren Zeichen hinweg

==**35. Preset**== ==– Auswahl des Arbeits-Presets,== ==**das standardmäßig geladen wird**== ==(0, 1, 2),== ==für den Betrieb des Funkgeräts.== ==**Kalibrierungen und Konfiguration sind für jedes Preset individuell**====!==

==*(für jedes Preset müssen Sie beim ersten Laden ein vollständiges Löschen des Speichers durchführen (Einschalten mit gedrückt gehaltenen PTT+EXIT), danach die Kalibrierungen und die Konfiguration laden (falls erforderlich) und alle benötigten Punkte einstellen).*==

==Das Umschalten auf das gewünschte Preset erfolgt im laufenden Betrieb, indem Sie das Funkgerät mit gedrückt gehaltener entsprechender Taste 0 / 1 / 2 einschalten.==

**36. Sql 2** – Empfindlichkeitsstufe der Rauschsperre für das Band **B**.

*Wenn Sie* ***SQL*** *(Menüpunkt 1) einstellen, wird die Einstellung gleichzeitig auf die Bänder* ***A*** *und* ***B*** *angewendet.*

*Wenn Sie* ***SQL2**** einstellen, wird eine separate Einstellung auf das Band* ***B*** *angewendet. (Die Einstellung des Bandes* ***B*** *wird jedes Mal zurückgesetzt, wenn* ***SQL*** *in Punkt 1 geändert wird.)*

**37. Loot** – das „Loot-Menü“ sammelt automatisch die Frequenzen, auf denen während des Suchlaufs im Spektrum und in VFO Empfang stattgefunden hat (128 Einträge – bei Überlauf werden die ältesten überschrieben. Sortiert ab der zuletzt gefundenen; ein Duplikatfilter wird angewendet und erkannte Subtöne werden angezeigt)

*Ist die Frequenz bereits im Speicher abgelegt, wird der Kanalname angezeigt. (Ist die Frequenz zweimal in der Kanalliste gespeichert, wird der Name des ersten Kanals in der Liste angezeigt.)*

*Zusätzlich wird die seit dem letzten Empfang vergangene Zeit angezeigt.*

*Wird ein Eintrag mit der Taste* ***M*** *ausgewählt, wird die aktuelle Frequenz in das aktive VFO-Band übernommen.*

*Das Speichern aus VFO in den Speicher erfolgt über Punkt 13. Mem_ch*

*Das „Loot-Menü“ wird nach einem Neustart des Funkgeräts geleert.*

### 2.4. Verstecktes Menü.

==***Ohne Erfahrung und ohne die erforderlichen Messgeräte wird davon abgeraten, die Parameter der Punkte 41-53 des versteckten Menüs zu verändern – eine Änderung dieser Punkte wirkt sich auf die Kalibrierung des Funkgeräts aus.***==

==***Jede Veränderung dieser Punkte erfolgt auf eigene Gefahr !!!***==

==***Es wird dringend empfohlen, vor dem Ändern ein BACKUP der Einstellungen und Kalibrierungen des Funkgeräts anzulegen!***==

Das versteckte Menü erscheint, wenn Sie das Funkgerät mit gleichzeitig gedrückt gehaltener **PTT** und seitlicher Funktionstaste **FN1** einschalten und danach alle Tasten loslassen *(lassen Sie* ***PTT + FN1*** *los, nachdem der Startbildschirm erloschen ist)*.

**38. F Lock** – Auswahl des Frequenzplans, der das Senden erlaubt *(die Eingabe einer Frequenz für Empfangszwecke bleibt im gesamten Bereich 15,0 MHz – 1349,9999 MHz offen):*

- **FCC** (144-148, 420-450);
- **CE** (144-146, 430-440);
- **GB** (144-148, 430-440);
- **LPD PMR** (433-435, 446-447) - dabei werden zusätzlich alle Fronttasten außer den Pfeiltasten ▲**/**▼ gesperrt (nach einem Neustart des Funkgeräts)

*Für ein Band im Frequenzmodus* ***VFO*** *kann eine Frequenz durch Blättern mit* ▲ */* ▼ *eingegeben werden (innerhalb eines VFO-Bandes).*

*Für ein Band im Kanalmodus* ***MR*** *können durch Blättern mit* ▲ */* ▼ *nur vorprogrammierte Kanäle ausgewählt werden;*

- **OFF** (136-240, 280-500) – der werkseitige Frequenzbereich.

**39. Tx All** – Auswahl des Modus der Sendesperre:

- **DEFAULT** – Senden in den im vorherigen Menüpunkt **36** gewählten Bändern**;**
- **DISABLE** – Senden auf allen Frequenzen verbieten;
- **ENABLE** – Senden auf allen Frequenzen erlauben.

**40. Sat** – stimmt die Empfangsfilter auf das Frequenzband Satcom um

- **OFF –** wenn die Spulen für den Satcom-Empfang modifiziert wurden;
- **ON –** wenn keine Modifikationen vorgenommen wurden.

==**41. F_Corr**== ==– Korrektur der Frequenz des Referenzoszillators==

==**42. r.Open**== ==– manuelle Einstellung des ÖFFNUNGS-Pegels der SQL nach RSSI.==

==**43. r.Close**== ==– manuelle Einstellung des SCHLIESS-Pegels der SQL nach RSSI.==

==**44. n.Open**== ==– manuelle Einstellung des ÖFFNUNGS-Pegels der SQL nach Rauschen.==

==**45. n.Close**== ==– manuelle Einstellung des SCHLIESS-Pegels der SQL nach Rauschen.==

==**46. g.Open**== ==– manuelle Einstellung des ÖFFNUNGS-Pegels der SQL nach Glitch.==

==**47. g.Close**== ==– manuelle Einstellung des SCHLIESS-Pegels der SQL nach Glitch.==

==**48. a**== ==– Service-Einstellungen für die Testfunktionen der Firmware====**.**==

==**49. b**== ==– Service-Einstellungen für die Testfunktionen der Firmware.==

==**50. c**== ==– Service-Einstellungen für die Testfunktionen der Firmware.==

==**51. d**== ==– Service-Einstellungen für die Testfunktionen der Firmware.==

==**52. e**== ==– Service-Einstellungen für die Testfunktionen der Firmware.==

**53. PWR** – Sendeleistung, in den Kalibrierungen gespeichert *(beim Aufrufen wird* ***0**** angezeigt; blättern Sie mit* ▲*/*▼ *oder drücken Sie* ***EXIT*** *- der Wert wird aktualisiert).*

*Um einen Wert zu speichern, wählen Sie zuerst die Frequenz / das Band und die Leistungsstufe, die Sie abgleichen möchten (HIGH / MID / LOW). Rufen Sie dann den Menüpunkt PWR auf, ändern Sie den Wert und drücken Sie* ***M*** *zum Speichern.*

***Der PWR-Wert ist für den Anfang, die Mitte und das Ende jedes Frequenzbandes sowie für jede Leistungsstufe unterschiedlich!!!***

## 3. TASTENFUNKTIONEN.

**Kurzer Druck** – drücken und loslassen (Standard).

**Langer Druck** – mindestens 1 Sekunde (bei den meisten Tasten entspricht dies der Kombination „**F + kurzer Druck**“).

**F + sehr langer Druck** – 5 Sekunden (bis die rote LED blinkt).

### ==3.1. Service-Kombinationen.==

==Funktionen, die beim Einschalten des Funkgeräts mit gedrückt gehaltenen Tasten verfügbar sind:==

==-== ==**PTT+FN1**== ==– Aufruf des versteckten Einstellungsmenüs (siehe Abschnitt 2.4).==

==-== ==**PTT+EXIT**== ==– Vollständiges Löschen des Speichers (Kalibrierungen, Konfiguration, alle Einstellungen) –== ==**muss bei ABGEZOGENEM Kabel erfolgen**====; halten Sie die Tasten nach dem Einschalten mindestens 2 Sekunden gedrückt.==

==-== ==**0**== ==– schnelle Auswahl von Preset 0 im Moment des Einschaltens (siehe Menüpunkt 35).==

==-== ==**1**== ==– schnelle Auswahl von Preset 1 im Moment des Einschaltens (siehe Menüpunkt 35).==

==-== ==**2**== ==– schnelle Auswahl von Preset 2 im Moment des Einschaltens (siehe Menüpunkt 35).==

### 3.2. Fronttasten.

**M**

- kurzer Druck **M** – Aufruf des Menüs
- kurzer Druck **M** – Verlassen des aktuellen Menüpunktes mit Bestätigung der Einstellung
- ==langer Druck== ==**M**== ==– Aufruf des Modem-Modus (TESTFUNKTION).==

▲/▼

- kurzer Druck ▲/▼ – Wechsel von Kanal / Frequenz um den eingestellten Schritt
- F+ kurzer Druck ▲/▼ – Wechsel von Kanal / Frequenz in 1-MHz-Schritten

**1 BAND**

- langer Druck **1** – Frequenzerfassung im Hintergrund (auf dem Display erscheint ein **x**)

==Bei eingeschalteter Hintergrunderfassung wird DW automatisch aktiviert.==

==*(Wird Aktivität erkannt, wird die erfasste Frequenz in den*== ==***Zwischenspeicher***== ==*von VFO2 kopiert (vorübergehend). Jede Manipulation an VFO2 lässt die erfasste Frequenz verschwinden. Die erfasste Frequenz kann im Loot-Menü eingesehen werden.)*==

*(Ist der Punkt* ***Roger=3*** *gesetzt (****empfohlen wird außerdem die Einstellung* *SQL=3, SAVE=1:3), arbeitet die Funktion als „Fernerfassung“; der Akkuverbrauch steigt und das Funkgerät kann träge reagieren.)*

- **F+** kurzer Druck **1** – Hinzufügen / Entfernen des aktiven Kanals zu bzw. aus den Suchlisten *(hinzufügen / entfernen ist nur in den Suchlisten 1 und 2 möglich* ***(****ein Druck auf F+1 fügt den aktuellen Kanal hinzu bzw. entfernt ihn und springt automatisch weiter zum nächstgelegenen Kanal, an dem derselbe Vorgang ausgeführt werden kann – beim Entfernen springt es zum nächsten Kanal, der aus der aktuellen Liste entfernt werden kann; beim Hinzufügen zum nächsten, der zur aktuellen Suchliste hinzugefügt werden kann)*, was durch das Erscheinen / Verschwinden des Symbols aus Punkt 9 auf S. 2 bestätigt wird.

Solange Suchliste 3 aktiv ist, können keine Kanäle hinzugefügt oder entfernt werden!

- F+ sehr langer Druck 1 – FM-Autobake (es erscheint der Text **RXTX**) (das Funkgerät antwortet auf einen Anruf mit einem „Piep“) – während der Aussendung kann die Autobake durch Druck auf eine beliebige Taste ausgeschaltet werden. Empfohlen wird **W/N=12.5**.
- Erneuter Druck F+ sehr lang 1 – Autobake mit Hintergrundüberwachung.

Die Laufzeit hängt von Punkt 19. TxTime ab, wobei 1 min = 10 s Bakenbetrieb / 2 min = 20 s Bake / … / 9 min = 90 s Bake / 10 min = 100 s Bake. Optimale Einstellungen: txfilt=1, mic=4, ste=on. Den Bakenmodus verlassen Sie mit **EXIT.**

**2 A/B**

- langer Druck 2 – Umschalten zwischen der oberen (A) und der unteren (B) Frequenz
- F+ sehr langer Druck 2 – FM-Autobake (es erscheint der Text **RXTX**) (das Funkgerät antwortet auf einen Anruf mit einem „Predator-Klickern“) – während der Aussendung kann die Autobake durch Druck auf eine beliebige Taste ausgeschaltet werden.

Erneuter Druck F+ sehr lang 2 – Autobake, die den DCS-Subton entsprechend dem Signalpegel setzt. Siehe die Tabelle des DCS in Abhängigkeit vom Signalpegel weiter unten.

*Praktisch zum Testen und Vergleichen verschiedener Antennen. Es zeigt nicht nur, dass das Signal die Bake erreicht hat, sondern auch die Stärke des empfangenen Signals.*

Den Bakenmodus verlassen Sie mit **EXIT.**

**Tabelle des DCS-Subtons der Bake F+2 / F+2 in Abhängigkeit vom Signalpegel**

| **DCS** | **dBm** | **DCS** | **dBm** | **DCS** | **dBm** | **DCS** | **dBm** | **DCS** | **dBm** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 023 | -120 | 143 | -096 | 266 | -072 | 445 | -050 | 662 | -026 |
| 025 | -119 | 145 | -095 | 271 | -071 | 446 | -049 | 664 | -025 |
| 026 | -118 | 152 | -094 | 274 | -070 | 452 | -048 | 703 | -024 |
| 031 | -117 | 155 | -093 | 306 | -069 | 454 | -047 | 712 | -023 |
| 032 | -116 | 156 | -092 | 311 | -068 | 455 | -046 | 723 | -022 |
| 036 | -115 | 162 | -091 | 315 | -067 | 462 | -045 | 731 | -021 |
| 043 | -114 | 165 | -090 | 325 | -066 | 464 | -044 | 732 | -020 |
| 047 | -113 | 172 | -089 | 331 | -065 | 465 | -043 | 734 | -019 |
| 051 | -112 | 174 | -088 | 332 | -064 | 466 | -042 | 743 | -018 |
| 053 | -111 | 205 | -087 | 343 | -063 | 503 | -041 | 754 | -017 |
| 054 | -110 | 212 | -086 | 346 | -062 | 506 | -040 |  |  |
| 065 | -109 | 223 | -085 | 351 | -061 | 516 | -039 |  |  |
| 071 | -108 | 225 | -084 | 356 | -060 | 523 | -038 |  |  |
| 072 | -107 | 226 | -083 | 364 | -059 | 526 | -037 |  |  |
| 073 | -106 | 243 | -082 | 365 | -058 | 532 | -036 |  |  |
| 074 | -105 | 244 | -081 | 371 | -057 | 546 | -035 |  |  |
| 114 | -104 | 245 | -080 | 411 | -056 | 565 | -034 |  |  |
| 115 | -103 | 246 | -079 | 412 | -055 | 606 | -033 |  |  |
| 116 | -102 | 251 | -078 | 413 | -054 | 612 | -032 |  |  |
| 122 | -101 | 252 | -077 | 423 | -053 | 624 | -031 |  |  |

| **DCS** | **dBm** | **DCS** | **dBm** | **DCS** | **dBm** | **DCS** | **dBm** | **DCS** | **dBm** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 125 | -100 | 255 | -076 | 431 | -052 | 627 | -030 |  |  |
| 131 | -099 | 261 | -075 | 432 | -051 | 631 | -029 |  |  |
| 132 | -098 | 263 | -074 |  |  | 632 | -028 |  |  |
| 134 | -097 | 265 | -073 |  |  | 654 | -027 |  |  |

Die Quansheng UV-K5 und ihre Varianten sind keine Labormessgeräte. Der Signalpegel wird von der S-Meter-Skala abgelesen und kann von Werten abweichen, die mit anderen Geräten gemessen wurden !!!

- instabiler Bereich (die AGC arbeitet)

Für stabile Messungen empfiehlt es sich, eine niedrige Sendeleistung einzustellen und einen gewissen Abstand zwischen den Funkgeräten einzuhalten.

**3 VFO/MR**
- langer Druck auf 3 – wechselt zwischen Frequenzmodus (**VFO**) und Kanalmodus (**MR**)
- F+ kurzer Druck auf 3 – (im **MR**-Modus) wechselt in den **VFO**-Modus und kopiert dabei automatisch die aktuelle Frequenz aus **MR** in das **VFO**. Im **VFO**-Modus wechselt F+ kurzer Druck auf 3 -> in den **MR**-Modus.
- F+ sehr langer Druck auf 3 – AM-Auto-Bake (der Text **RXTX** erscheint) (das Funkgerät beantwortet einen Ruf mit einem amplitudenmodulierten Signal) – während der Aussendung lässt sich die Auto-Bake durch Drücken einer beliebigen Taste abschalten. Den Bakenmodus verlassen Sie mit **EXIT.**

**4 FC**
- langer Druck auf **4** – die Frequenzliste Loot. Funktionen im Loot-Menü:
***4*** *– fügt eine Frequenz zur Blacklist (Lock) hinzu bzw. entfernt sie daraus, bis zum Ausschalten.*
***0*** *(lang) – löscht die Loot-Blacklist und die ATT-Liste.*
***M*** *– sendet die aktuelle Frequenz an das aktive Band* ***VFO*** *(ist* ***MR*** *aktiv und existiert ein Kanal mit dieser Frequenz, schaltet das Funkgerät auf diesen Kanal um). Das Speichern aus dem VFO erfolgt über Punkt 13. Mem_ch.*
*Beim Ausschalten des Funkgeräts wird die Loot-Liste gelöscht.*
- F+ langer Druck auf 4 – Frequenzerfassung; speichern Sie die Frequenz mit der Taste **M**.
Standardmäßig sind die UHF/VHF-Filter deaktiviert, wie in der Originalfirmware, sodass nur starke lokale Signale oder Funkgeräte in unmittelbarer Nähe erfasst werden. Um Reichweite und Stabilität der Erfassung zu verbessern, wählen Sie mit 1 (VHF) oder 2 (UHF) den benötigten Filter.

*Im Erfassungsmodus "springen" die Frequenz und der Subton auf dem Display (Sie sehen, wie Werte durchlaufen werden), bis eine Erfassung stattfindet. Sobald die erfasste Frequenz bestimmt ist, bleibt der Wert stehen.*

- F+ sehr langer Druck auf 4 – wechselt in den PTT-Holder-Modus (hält die Aussendung, bis PTT erneut gedrückt wird). Die Aussendung wird direkt durch gleichzeitiges Drücken von

**PTT+FN1** eingeschaltet.
Den PTT-Holder-Modus verlassen Sie durch erneutes Drücken von **PTT**.

**5 NOAA**
- langer Druck auf 5 – schaltet den Spektrumanalysator mit Hybrid-Rauschsperre ein
- F+ kurzer Druck auf 5 – startet den Spektrumanalysator mit Nachführung der Frequenz des aktiven **VFO / MR**

**6 H/M/L**
- langer Druck auf 6 – schaltet die Sendeleistung **HIGT / MID / LOW** um

**7 VOX**
- langer Druck auf 7 – ändert die Modulation **FM / AM / USB**
- F+ kurzer Druck auf 7 – ändert die Kanalbandbreite **12.5 / 25 kHz**
- F+ sehr langer Druck auf 7 – AM-Tongenerator. Tasten:
**1, 2, 3** – Tastverhältnis; **4, 5, 6** – Verzögerung; **7, 8, 9** – Bandbreite (~25-1000k);
**0** – Beimischen eines FM-Tons; ▲**/**▼ – Feineinstellung der Verzögerung.

**8 R**
- langer Druck auf 8 – schaltet den Reverse-Modus ein: Empfangs- und Sendefrequenz werden vertauscht (neben der Bandbreite erscheint das Symbol R)
- F + sehr lang 8 – Randomizer für Frequenz und Leistung (das Symbol **r** erscheint) *(ein Druck auf PTT bei aktivem F und eingeschaltetem Randomizer – sendet mit abgeschaltetem Mikrofon)*

**9 Call**
- langer Druck auf 9 – dynamische Lautstärke (das Symbol **D** erscheint)
(hilft mitunter, Rauschen/Knacken am Ende einer Aussendung zu glätten)
- F+ kurzer Druck auf 9 – fügt den Kanal zur Prioritätsliste hinzu, die beim Scannen verwendet wird *(2 Kanäle in ScList1 und 2 Kanäle in ScList2, die alle 3 Schritte der Suchliste abgefragt werden); ein drittes Drücken von F+9 schaltet die Prioritätskanäle ab. Auf dem Display wird nichts angezeigt. Wird derselbe Kanal zweimal in die Prioritätsliste aufgenommen, kann der Suchlauf "hängen bleiben".*

**0 FM**
- langer Druck auf 0 – schaltet das FM-Radio ein/aus (Sie können es mit EXIT verlassen)
*Der FM-Empfang wird unterbrochen, sobald ein Signal erscheint, und 5 Sekunden nach dem Verschwinden des Signals fortgesetzt. PTT unterbricht den FM-Empfang ebenfalls vorübergehend.*
***Bedienung im FM-Radio-Modus:***
▲*/*▼ *- Kanal / Frequenz wechseln;* ***F+1*** *- VFO / MR umschalten;* ***F+3*** *– Sendersuche (sobald ein Sender gefunden wurde, pausiert die Suche, ohne automatisch zu speichern.* ▲*/*▼ *- Suche fortsetzen);* ***M*** *- Kanal löschen (in MR), Kanal speichern (in VFO);* ***F+6*** *– AGC (automatische Verstärkungsregelung) ein-/ausschalten*
- F+ sehr langer Druck auf 0 – stellt automatisch den Subton des letzten Empfangs ein (das Symbol **A** erscheint)

**`*` SCAN**
- kurzer Druck auf `*` – schaltet das Dämpfungsglied für die aktuelle Frequenz / den aktuellen Kanal ein (**ATT1** erscheint, beim nächsten Druck – **ATT2**, dann **ATT3**, der vierte Druck schaltet es aus);
- langer Druck auf `*` – startet im Frequenzmodus den Frequenzsuchlauf, im Kanalmodus den Kanalsuchlauf *(gemäß der im Menüpunkt 24.SList gewählten Suchliste. Wurden der gewählten Suchliste keine Kanäle hinzugefügt, reagiert das Funkgerät unter Umständen nicht mehr)*, (Abbruch mit **EXIT**).
*Wenn Sie beim Suchlauf einen Kanal / eine Frequenz überspringen möchten, können Sie dafür ATT1, ATT2 oder ATT3 einschalten;*
- F+ kurzer Druck auf `*` – sucht CTCSS-Subtöne auf der aktuellen Frequenz.

==Nach Abschluss des Suchlaufs lässt sich mit der Taste== ==**M**== ==der gefundene Subton als Sende-Subton für das aktive VFO-Band übernehmen.==

**F #**
- kurzer Druck auf F – aktiviert den Optionsmodus (das Symbol **F** erscheint)
- langer Druck auf F – schaltet die Sperre der Fronttasten ein/aus (**L** erscheint)
- Solange die Anzeige **F** leuchtet und die Randomizer-Funktion eingeschaltet ist (siehe Abschnitt 3.1, Punkt 8 R), sendet ein Druck auf PTT mit abgeschaltetem Mikrofon.

### 3.3. Seitentasten.

**WICHTIG !!!** Wenn bei der Konfiguration des Funkgeräts über CHIRP oder PSCPS FN1 und/oder FN2 auf NONE (nicht belegt) gesetzt werden, kann das Funkgerät gesperrt werden und beim Einschalten nach einem Code fragen.

![screenshot](images/p16_1.png)

**Seitliche "Sprechtaste" [PTT]**

- Drücken startet die Aussendung auf dem Band
- Drücken zusammen mit einer beliebigen Fronttaste sendet einen **DTMF**-Code

**Seitliche Funktionstaste [FN1]**
**(Standardwerte)**

- kurzer Druck – öffnet/schließt die Rauschsperre
- langer Druck – schaltet die Taschenlampe ein/aus

**Seitliche Funktionstaste [FN2]**
**(Standardwerte)**

- kurzer Druck – schaltet die Sendeleistung **HIGT / MID / LOW** um
- langer Druck – startet die Rundsendebake auf der gewählten Frequenz *(funktioniert, wenn Menüpunkt 17 -* ***DW*** *ausgeschaltet ist; Abbruch mit* ***EXIT****)*
- Drücken bei gehaltener PTT sendet einen Ton von **1750 Hz**

Wird die Firmware über eine Originalfirmware oder zusammen mit einer eigenen Konfigurationsdatei installiert, können die Standardbelegungen der Tasten [FN1] und [FN2] abweichen, da diese Belegungen in der Konfigurationsdatei gespeichert sind.

**Benutzerfunktionen der Tasten [FN1] und [FN2]**

Die Funktionen von FN1 und FN2 lassen sich nur über Software (zum Beispiel CHIRP) ändern und können nicht über das Menü des Funkgeräts eingestellt oder neu belegt werden.

**Folgende Auswahlmöglichkeiten stehen zur Verfügung:**

**NONE** – nichts gewählt,

**FLASH LIGHT** – Taschenlampe,
**POWER** – Sendeleistung umschalten, **MONITOR** – Rauschsperre öffnen,
**SCAN** – Suchlauf,

**VOX** – sprachgesteuerte Aussendung,
**FM RADIO** – FM-Radio,

**1750 Hz** – einen Ton von 1750 Hz senden

### 3.4. Frequenzeingabe im Hauptbildschirm.

Um eine Frequenz im Hauptbildschirm von Hand einzugeben, müssen Sie zunächst in den Frequenzmodus wechseln (zwischen Frequenz- und Kanalmodus schalten Sie mit einem langen Druck auf die Taste **3 VFO/MR** um). Links im Display, gegenüber der Frequenz, erscheint dann **VFO**.
Geben Sie anschließend die Frequenz ein.
Für die Eingabe des Dezimaltrennzeichens dient die Taste

**Beispiele:** 140 *→* = 140.00000 oder 433*875 *→* = 433.87500

Abbrechen lässt sich die Frequenzeingabe mit der Taste

### 3.5. Suchlauf in den Modi VFO und MR.

**Suchlauf innerhalb festgelegter Frequenzgrenzen im VFO-Modus**

- VFO1 und VFO2 in den Frequenzmodus schalten
- die Anfangsgrenze (VFO1) und die Endgrenze (VFO2) des Suchlaufs einstellen
- das obere VFO1 zum aktiven machen
- den Suchlauf mit einem langen Druck auf die Taste **`*` Scan** starten
- er läuft in einer Schleife innerhalb der Grenzen (von VFO1 bis VFO2)
- die Tasten ▲**/**▼ ändern die Suchrichtung
- beendet wird der Suchlauf mit **EXIT**
(die Frequenz kehrt dann auf ihren Ausgangswert zurück – VFO1)

*Hinweis 1: Starten Sie den Suchlauf, während VFO2 aktiv ist, läuft der Suchlauf außerhalb der eingestellten Grenzen, und beim Beenden kehrt die Frequenz nicht auf ihren Ausgangswert zurück.*

*Hinweis 2: Die Schrittweite des Suchlaufs = die für Band A eingestellte Schrittweite (Punkt 2 des Einstellungsmenüs).*

**Suchlauf im Kanalmodus (MR)**

- in den Kanalmodus schalten
- bei Bedarf im Menüpunkt 24 SList1, SList2 oder SList3 auswählen
- den Suchlauf mit einem langen Druck auf die Taste **`*` Scan** starten
- er läuft in einer Schleife gemäß der gewählten SList
- die Tasten ▲**/**▼ ändern die Suchrichtung
- bleibt der Suchlauf wegen Störungen auf einem der Kanäle hängen, können Sie für diesen Kanal durch Drücken von **`*`** das Dämpfungsglied einschalten (**ATT1** oder **ATT2**)
- beendet wird der Suchlauf mit **EXIT**

- ==Die Funktion **CHANNEL = PRESET**:==
- ==die Endfrequenz im Offset einstellen, Shift – scn (die Suchrichtung) einstellen, den Kanal zur gewünschten Suchliste hinzufügen.==
- ==Nach dem Start eines Suchlaufs im Kanalmodus wird beim Erreichen dieses Kanals zusätzlich ein Suchlauf innerhalb der Grenzen dieser Einstellung durchgeführt.==

## 4. SPEKTRUMANALYSATOR

### 4.1. Haupt-Spektrummodus (Hybrid-Rauschsperre) — so rufen Sie ihn auf:

- langer Druck auf **5** – schaltet den Spektrumanalysator mit Hybrid-Rauschsperre ein
- **F** + kurzer Druck auf **5** – startet das Spektrum mit Frequenznachführung im VFO
- **WICHTIG!** *Wird der Spektrumanalysator aus einem Kanal oder aus dem VFO mit eingeschaltetem RX/TX-Offset gestartet (Punkte 8 und 9 des Einstellungsmenüs), so wird dieser Offset auch beim Senden aus dem aktiven Frequenzerfassungsmodus angewendet.*

![screenshot](images/p19_1.png)

![screenshot](images/p19_2.png)

**Der Spektrumanalysator verwendet eine Hybrid-Rauschsperre:**

Wird die Schwelle der Rauschsperre abgesenkt, öffnet sie nur bei Signalen, die eher Kanalsignalen ähneln, also eine übliche Bandbreite und Frequenz haben.

1. Preset (Frequenzplan) – **3 / 9**
2. Anzahl der Suchschritte – **2 / 8**
3. Schrittweite des Suchlaufs – **1 / 7**
4. Aktuelle oder zuletzt erkannte Empfangsfrequenz (die, auf der ein Signal gefunden wurde) – die Frequenz ändert sich, wenn ein Signal mit einem Pegel oberhalb der Schwelle der Rauschsperre (10) erkannt wird.

5. Kanalname (wird angezeigt, sofern die Frequenz bereits im Speicher des Kanalmodus (MR) abgelegt ist. Ist die Frequenz zweimal in der Kanalliste gespeichert, wird der Name des ersten Kanals der Liste angezeigt. Ist der Kanal gespeichert, ihm aber kein Name gegeben worden, wird «**,,,,,,,,,**» angezeigt — wie Sie einem Kanal einen Namen geben, steht in der Beschreibung zu Punkt **34 Rename** des Einstellungsmenüs)
6. Subton des empfangenen Signals (wird angezeigt, falls vorhanden)
7. Empfängerbandbreite – **6**
8. Modulationsart AM/FM/USB – **0**
9. Ladezustandsanzeige des Akkus
10. Pegel der Rauschsperre (SQ) – `*` / **F**
11. Anfangsfrequenz des Suchbereichs – Sie können den gesamten Bereich mit ▲/▼ verschieben oder die Anfangsfrequenz über die Tastatur eingeben: **5** drücken, dann im Modus "freie Eingabe" die neue Anfangsfrequenz unmittelbar nach dem Erscheinen von ----- eingeben; im Preset-Modus mit **F** **f start** auswählen, die MHz, das Trennzeichen `*`, die kHz und Hz eingeben und dann mit **M** übernehmen.
12. Frequenzschritt des Spektrums – **4** (dient dazu, den gesamten abgetasteten Bereich mit ▲/▼ um die eingestellte Schrittweite zu verschieben)
13. Endfrequenz des Suchbereichs – Sie können den gesamten Bereich mit ▲/▼ verschieben oder die Endfrequenz über die Tastatur eingeben: **5** drücken, mit **F** **f end** auswählen, die MHz, das Trennzeichen `*`, die kHz und Hz eingeben und dann mit **M** übernehmen *(im Modus "freie Eingabe" wird die Endfrequenz entsprechend Anzahl und Größe der Schritte korrigiert, in Vielfachen von 16/32/64/128; im Preset-Bearbeitungsmodus wird die exakte Frequenz gesetzt).*

**langer Druck auf 4** – Loot aufrufen. Funktionen im Loot-Menü:

***4*** *– fügt die Frequenz bis zum Ausschalten zur Blacklist (Lock) hinzu.*

***0*** *– löscht die Loot-Blacklist des Spektrums.*

*Beim Ausschalten des Funkgeräts wird die Loot-Liste gelöscht.*

### 4.2. Zusätzliche Funktionstasten im Spektrumanalysator-Modus:

**FN1** – fügt die aktuelle Frequenz zur Blacklist des Suchlaufs hinzu (128 Frequenzen – bei Überlauf werden die ältesten überschrieben) – so lange drücken, bis die rote LED zum ersten Mal blinkt (nach dem zweiten Blinken der LED wird die Blacklist gelöscht).

- Die Blacklist wird zurückgesetzt, nachdem das Funkgerät AUS/EIN geschaltet wurde.
- Wenn Sie einige Frequenzen mit ständigen Störungen dauerhaft behalten möchten, können Sie sie in die gespeicherte Blacklist übernehmen. Gehen Sie dazu in das Menü Presets (Aufruf mit **M**, Blättern mit **M**, dann **SAVE** wählen) und drücken Sie anschließend nach oben ▲ (damit werden die letzten 16 Frequenzen der Blacklist gespeichert).
- Die gespeicherte Blacklist wird mit einem **langen Druck auf FN1** gelöscht – so lange, bis die rote LED zum zweiten Mal blinkt (im Spektrum), anschließend im Menü Presets speichern.

***!!! Damit die gespeicherte Blacklist korrekt arbeitet***, *empfiehlt es sich, beim ersten Start des Scanners nach der Installation der Firmware die Blacklist mit einem langen Druck auf FN1 zu löschen und zu speichern.*

**FN2** – Frequenz überspringen – während des Empfangs eines Signals drücken (die Frequenz wird nur im aktuellen Suchdurchlauf übersprungen; im nächsten Durchlauf nimmt sie wieder am Suchlauf teil)

– schaltet die Displaybeleuchtung im Spektrummodus aus / ein (drücken, wenn nichts empfangen wird).

### 4.3. Einstellungen des Spektrumanalysators.

Im Spektrumanalysator können Sie entweder im Modus "freie Eingabe" (Bereich) oder mit vordefinierten Presets arbeiten. Die Einstellungen der "freien Eingabe" werden nicht gespeichert und beim Aus-/Einschalten des Funkgeräts gelöscht. Änderungen an den Presets lassen sich bei Bedarf speichern.

Standardmäßig sind für den Suchlauf im Spektrumanalysator-Modus die folgenden Presets eingerichtet und vorkonfiguriert:

| Preset | Bereich, MHz | Schritt | Modulation | Bandbreite |
|---|---|---|---|---|
| — | 28.89000 – 24.97000 | 5 kHz | SSB | 6.25 kHz |
| CB | 26.97500 – 27.99900 | 5 kHz | FM | 25 kHz |
| 10m | 28.00000 – 29.20000 | 5 kHz | SSB | 6.25 kHz |
| 7m | 40.00000 – 43.00000 | 25 kHz | FM | 25 kHz |
| 6m | 50.00000 – 52.00000 | 12.5 kHz | FM | 25 kHz |
| Air | 115.00000 – 140.00000 | 50 kHz | AM | 25 kHz |
| 2m | 144.00000 – 146.00000 | 25 kHz | FM | 25 kHz |
| Rail | 151.75000 – 154.95000 | 25 kHz | FM | 25 kHz |
| Sea | 156.02500 – 159.22500 | 25 kHz | FM | 25 kHz |
| Sat | 240.00000 – 243.80000 | 5 kHz | FM | 25 kHz |
| Riv1 | 300.01250 – 300.51250 | 12.5 kHz | FM | 25 kHz |
| Riv2 | 336.01250 – 336.81250 | 12.5 kHz | FM | 25 kHz |
| 402 | 402.00000 – 403.60000 | 12.5 kHz | FM | 25 kHz |
| 430 | 430.00000 – 433.00000 | 25 kHz | FM | 25 kHz |
| LPD | 433.07500 – 434.99900 | 25 kHz | FM | 25 kHz |
| 435 | 435.00000 – 445.99900 | 25 kHz | FM | 25 kHz |
| PMR | 446.00000 – 446.99900 | 6.25 kHz | FM | 25 kHz |
| 450 | 450.00000 – 461.99900 | 25 kHz | FM | 25 kHz |
| 462 | 462.00000 – 471.00000 | 12.5 kHz | FM | 25 kHz |
| LoRa | 864.02500 – 869.00000 | 50 kHz | FM | 25 kHz |
| GSMu | 890.02500 – 915.00000 | 100 kHz | FM | 25 kHz |
| GSMd | 935.02500 – 960.00000 | 100 kHz | FM | 25 kHz |
| 23cm | 1240.00000 – 1300.0000 | 100 kHz | FM | 25 kHz |

**WICHTIG:**
Die Presets lassen sich an Ihre Bedürfnisse anpassen, beachten Sie dabei jedoch:

- Die Namen der Presets können nicht bearbeitet werden.
- Änderungen an Bandbreite und Modulation werden nicht gespeichert.

### 4.3.1. Arbeiten im Modus "freie Eingabe"

Die freie Eingabe ist nicht an ein bestimmtes Band gebunden, und ihre Einstellungen werden nicht gespeichert.

Um die Anfangsfrequenz des Suchbereichs einzustellen, drücken Sie **5** – das Eingabefenster für die Anfangsfrequenz des Suchlaufs öffnet sich (---------). Geben Sie die Anzahl der MHz ein, das Dezimaltrennzeichen mit `*`, danach die Stellen für kHz und Hz. Drücken Sie **M**, um den eingegebenen Wert zu bestätigen.

Im Modus "freie Eingabe" wird die Endfrequenz automatisch aus der Schrittweite – 1 / 7 – und der Anzahl der Schritte – 2 / 8 – gebildet (*wenn Sie versuchen, die Endfrequenz des Suchlaufs über* ***f end*** *zu ändern, wird die Endfrequenz an die Anzahl der Schritte in Vielfachen von 16/32/64/128 angepasst*).

Wird die Anfangsfrequenz des Suchlaufs geändert, verschiebt sich der gesamte Bereich mitsamt allen seinen Einstellungen — Anzahl der Schritte, Schrittweite, Modulation und so weiter — auf die neue Anfangsfrequenz. *(Beispiel: Sie haben den Bereich 400–401.6 MHz (1.6 MHz breit) / 128×1 Schritte mit 12.5 kHz Bandbreite abgetastet. Geben Sie nun 5 -> ------- -> 510 -> M ein, verschiebt sich der gesamte Bereich von 400–401.6 auf 510–511.6, und alle übrigen Einstellungen bleiben erhalten)*

Zum Ändern von Modulation, Schrittweite, Bandbreite und so weiter – siehe Abschnitt 4.1.

Um exakte Werte für den Suchbereich festzulegen, müssen Sie die Einstellungen des Preset-Modus verwenden.

### 4.3.2. Presets bearbeiten:

Um den Frequenzbereich eines Presets zu bearbeiten, drücken Sie **5** – das Eingabefenster für die Anfangsfrequenz des Suchlaufs öffnet sich (---------). Wählen Sie mit **F** den zu ändernden Parameter: die Anfangsfrequenz (**f start**) und / oder die Endfrequenz (**f end**) des Presets. Geben Sie die Anzahl der MHz ein, das Dezimaltrennzeichen mit `*`, die Anzahl der Hz, und drücken Sie dann **M** (die Werte werden beim Neustart des Funkgeräts zurückgesetzt, sofern Sie sie nicht über das Zusatzmenü speichern).

- Neben der Frequenz lassen sich in den Preset-Einstellungen auch die Anzahl der Suchschritte und die Schrittweite ändern.
- Wenn Sie außer der Frequenz auch die Schrittweite ändern möchten, ändern Sie ZUERST die Anfangsfrequenz, dann die Schrittweite, dann die Endfrequenz; danach können Sie **SAVE** ausführen.

**ACHTUNG:** Beim Bearbeiten der Presets ist es wichtig, deren ursprüngliche Reihenfolge beizubehalten *(es ist nicht ratsam, den Bereich 144–148 MHz in 27–50 MHz zu ändern)*, und ebenso, einander überlappende Bereiche zu vermeiden *(Presets mit 144–149 / 146–200 / 188–205 führen zu einem Konflikt).*

### 4.3.3. Einstellen der zusätzlichen Parameter des Spektrumanalysators:

Drücken Sie **M** – oben erscheint der erste Parameter des Zusatzmenüs (**Mult: OFF**); jeder weitere Druck auf **M** blättert in einer Schleife durch die Parameter. Bleiben Sie bei dem gewünschten Parameter stehen und wählen Sie mit ▲ (übernehmen bzw. ein) / ▼ (abbrechen bzw. aus) den gewünschten Wert (Zustand) dieses Parameters.

**Kurzbeschreibung der zusätzlichen Parameter des Spektrumanalysators:**

**Mult** – Multi-Preset, Abtasten aller gewählten Presets nacheinander (Tasten **3/9** – Preset auswählen; Taste **4** – Preset zum Suchlauf hinzufügen bzw. davon ausschließen (hinzugefügte Presets sind mit dem Zusatz fc gekennzeichnet); langer Druck auf **4** – alle Presets vom Multi-Scan ausschließen; Taste nach oben ▲ – Start; zum Verlassen des Multi-Preset-Modus **M** + nach unten ▼ drücken oder **EXIT**)

**ATT** – Dämpfungsglied

**Turbo** – Turbo-Suchlaufmodus (ein – ▲ / aus – ▼) – Abtasten im beschleunigten Modus: Genauigkeit und Empfindlichkeit sind geringer, die Geschwindigkeit ist dafür höher, sodass schwache Signale übersehen werden können. Lässt sich mit save:on speichern

**SQ** – Pegel der Störunterdrückung für den hybriden Teil des Spektrums

**Delay** – Bewertungszeit des Signals (höhere Werte erhöhen die Empfindlichkeit, verlangsamen aber den Suchlauf, und umgekehrt)

**Lna** – schaltet den rauscharmen Vorverstärker ein (im Gegensatz zu **LNA_hi** aus Punkt 29 des Hauptmenüs hat er einen höheren Verstärkungswert – etwa 10 % stärker)

**EXP** – Modus "Spektrum-Belichtung" (mit den Tasten `*` und **F** können Sie anstelle des Balkens für die Schwelle der Rauschsperre den Cursor bewegen, um die Frequenz der Pegelspitzen abzulesen)

**SAVE** – speichert die Einstellungen einschließlich der Presets dauerhaft im Speicher (nach oben ▲ – schreiben, nach unten ▼ – zurück)

**ECO** – Sparmodus, der durch Verlangsamung des Suchlaufs wirkt

### 4.4. Aktiver Frequenzerfassungsmodus — "Detailansicht".

**VFO-PRO (Aufruf aus dem Haupt-Spektrummodus durch Drücken von PTT)**

![screenshot](images/p24_1.png)

Im Frequenzerfassungsmodus werden beim Senden mit PTT der Offset und der Subton angewendet, sofern diese Frequenz mit diesen Einstellungen im Speicher abgelegt wurde.

![screenshot](images/p24_2.png)

![screenshot](images/p24_3.png)

1. S-Meter-Skala
2. Die aus dem "Loot-Menü" gefundenen Kanäle lassen sich durchblättern – **1 / 7;** zur Blacklist hinzufügen – **4**
3. Pegel der Rauschsperre – `*` / **F**
4. Aktuelle Empfangsfrequenz (Abstimmung – ▲**/**▼)
5. Für die aktuelle Frequenz gefundener Subton (falls vorhanden)
6. Modus zum Einstellen der Register – **M / EXIT**

### 4.5. Register des aktiven Frequenzerfassungsmodus.

Solange AM FIX ausgeschaltet ist, werden die manuellen LNA- und PGA-Einstellungen bis zum Neustart des Funkgeräts nicht zurückgesetzt.

Die Parameter DEV und Tx3k werden beim Verlassen des Spektrumanalysators in die Kalibrierdaten geschrieben.

**xtal** – Feineinstellung der Empfangsbandbreite (für nicht normgerechte Signale). (Werkseinstellung = 2)

**LNAs** – Grobeinstellung des rauscharmen Vorverstärkers LNA (Werkseinstellung = 3)

**LNA** – Feineinstellung des rauscharmen Vorverstärkers LNA

Wenn Sie die Punkte **LNA** und **LNAs** in den Registern des aktiven Frequenzerfassungsmodus ändern und anschließend speichern, schaltet der Menüpunkt 29 **LNA_hi** auf manuelle Steuerung (**MAN**) um.
Um zur automatischen Steuerung zurückzukehren, öffnen Sie das Einstellungsmenü, drücken Sie beim Punkt 29 **LNA_hi** zweimal **M** (**LNA_hi** wechselt auf **ON**) und speichern Sie die Einstellungen anschließend im Presets-Menü, indem Sie **SAVE: ON –** ▲ wählen.

**DEV** – Bandbreite des Sendekanals (Werkseinstellung = 1280)
(empfohlen wird ein Wert zwischen 1200 und 1450, Standard = 1400)

**SCR** - manuelle Einstellung der Inversionsfrequenz des Scramblers bei eingeschaltetem Scrambler.
(Standard = 5150)

**Tx3k** – Einstellung der Sendemodulation (Standard = 65531)
(bleibt gespeichert, bis der Menüpunkt 33 - **tx_filt** angewendet wird)
Für Tx3k haben sich die folgenden Werte bewährt:

- 62731 – Werkseinstellung
- 44831 – optimal
- 37431 – übersteuert (für SATCOM und PMR)

**03t** – Feineinstellung der Breite des Audiofilters (300 Hz), für TX
(Standard = 36873; optimal = 36600)

**AFC** - schaltet die automatische Empfangsfrequenzregelung ein

**AFCR (AFC range)** – legt den AFC-Bereich fest (stabil bei 1-5 / optimal = 6)

**c0db** – Mikrofoneinstellung

**P (Peak (rssi))** – alternative Feldstärkeanzeige für starke Signale
(funktioniert am besten bei Frequenzen über 1 GHz)

### 4.6. Tastenbelegung in den Modi des Spektrumanalysators

| **Taste** | **Modus** | **Funktion** |
| --- | --- | --- |
| **M** | Hauptmodus | Wählt den zusätzlich einzustellenden Parameter aus |
| | Frequenzerfassung | Wählt das zu bearbeitende Register aus |
| ▲<br>▼ | Hauptmodus | Stimmt die Spektrumfrequenz ab |
| | Einstellung des Zusatzparameters | Ändert den Parameterwert |
| | Frequenzerfassung | Stimmt die Frequenz ab |
| | Registerbearbeitung | Ändert den Registerwert |
| **EXIT** | Alle Modi | Abbrechen / Zurück |
| **PTT** | Hauptmodus | Wechselt in den Frequenzerfassungsmodus |
| | Frequenzerfassung | Startet die Aussendung, "TX" |
| **FN1** | Hauptmodus | Fügt die aktuelle Frequenz zur Blacklist hinzu<br>(*die RX/TX-LED blinkt zur Bestätigung der Auswahl rot*)<br>*Es findet keine Aussendung statt, dies ist nur eine Anzeige!!!* |
| | Frequenzerfassung | Schaltet die Rauschsperre aus / ein |
| **FN2** | Hauptmodus | Schaltet die Hintergrundbeleuchtung aus / ein (wenn nichts empfangen wird)<br>Überspringt die Frequenz im aktuellen Suchlauf (während ein Signal empfangen wird) |
| | Frequenzerfassung | Schaltet die Hintergrundbeleuchtung aus / ein |

## 5. HÄUFIG GESTELLTE FRAGEN, MÖGLICHE PROBLEME UND IHRE LÖSUNG.

| **Nr.** | **Probleme**<br>**Fragen** | **Lösung**<br>**Anmerkungen, Antworten auf Fragen.** |
| --- | --- | --- |
| ==1== | ==Beim Einschalten des Funkgeräts erscheint Schnee (Bildrauschen) auf dem Display.== | ==Sie müssen das Funkgerät bereinigen (siehe Abschnitt 3.1. Service-Tastenkombinationen) und anschließend die Kalibrierdaten laden (zuerst Ihre eigene Werkskalibrierung, danach die mit der Firmware gelieferte Kalibrierung).== |
| ==2== | ==Beim Versuch, die Frequenz im VFO-Modus zu ändern, wird die Frequenz nicht übernommen== | ==1. Prüfen Sie, ob die im Punkt 2.Step eingestellte Schrittweite zu der von Ihnen benötigten Frequenz passt.==<br>==2. Wahrscheinlich wurde der Bereinigungsvorgang nach der Installation der Firmware nicht korrekt abgeschlossen (das Servicekabel wurde während der Bereinigung nicht abgezogen). – Führen Sie die Bereinigung erneut durch / laden Sie die Kalibrierdaten / nehmen Sie die Einrichtung vor.== |
| 3 | Auf welchen Frequenzen darf ich senden? | Es gibt zivile Funkfrequenzen, die zur freien Nutzung freigegeben sind. In der Regel sind das:<br>CB (25.165 – 29.445 MHz) mit einer Sendeleistung von 4.0-12.0 W<br>LPD (433.075 – 434.775 MHz) mit einer Sendeleistung von 0.01 W<br>PMR (446.00625 – 446.19375) mit einer Sendeleistung von 0.5 W<br>In einigen Ländern werden außerdem die Bänder FRS und GMRS genutzt. |
| 4 | Auf welchen Frequenzen darf ich nicht senden? | Ohne besondere Genehmigungen ist das Senden außerhalb der zivilen Bänder gesetzlich verboten. Alle übrigen Frequenzbänder werden von anderen Funkdiensten genutzt, von Funkamateuren bis zu Behörden, darunter Satelliten, Mobilfunknetze, Fluglotsen und Luftfahrzeuge, Wetterstationen, Binnenschifffahrt und Seefunk, Militär und andere. Wenn Sie den Betrieb eines dieser Dienste stören, können Sie nach dem in Ihrem Land geltenden Recht zur Verantwortung gezogen werden. |
| 5 | Auf welchen Frequenzen arbeiten Empfänger und Sender des Quansheng UV-K5 | In der Karina-Firmware sind Empfang und Aussendung auf allen Bändern freigeschaltet (siehe Abschnitt 2.2. Arbeitsfrequenzbänder (Bands)).<br>Bei Funkgeräten ohne Hardware-Modifikationen dürfen Sie nur in den vom Hersteller angegebenen Arbeitsbändern senden, ohne das Gerät zu zerstören: 136-174 MHz / 400-470 MHz |
| 6 | Was passiert, wenn ich ohne Antenne sende? | Das Senden ohne Antenne oder mit einer auf ein anderes Frequenzband abgestimmten Antenne zerstört die Endstufe des Funkgeräts. |
| 7 | Sendet das Funkgerät im CB-Band? Kann ich mit | In der Karina-Firmware ist das 27-MHz-Frequenzband standardmäßig für Empfang und Aussendung freigeschaltet.<br>Zum Empfang müssen Sie eine auf dieses Frequenzband abgestimmte Antenne anbringen.<br>Das Senden in diesem Frequenz |

| **Nr.** | **Probleme**<br>**Fragen** | **Lösung**<br>**Anmerkungen, Antworten auf Fragen.** |
| --- | --- | --- |
| | Lkw-Fahrern sprechen? | band ergibt mit Funkgeräten ohne Hardware-Modifikation jedoch keine brauchbare Verbindung (weil die Sendeleistung viel zu gering ist); gleichzeitig erzeugt der Versuch, in diesem Band zu senden, aufgrund der physikalischen Eigenschaften des Funkgeräts Störungen im Flugfunkband und zerstört außerdem die Endstufe des Funkgeräts. |
| 8 | Warum hört mich auf CB niemand? | Im Werkszustand überschreitet die Sendeleistung des Funkgeräts im CB-Band 0.01 W nicht. Ohne physische Modifikationen ist das Senden in diesem Frequenzband daher nicht nur nutzlos, sondern auch gefährlich für das Funkgerät selbst. |
| 9 | Warum ist die Verbindung im Auto schlecht? | Die Karosserie schirmt Funksignale ab. Für eine stabile Verbindung wird empfohlen, eine Außenantenne außerhalb der Karosserie anzubringen. |
| 10 | Wozu das Funkgerät überhaupt flashen | Ein Funkgerät im Werkszustand arbeitet "ab Werk" zuverlässig und erfüllt seine Funktionen. Eine modifizierte Firmware erweitert den Funktionsumfang des Funkgeräts und bietet zusätzliche und flexiblere (professionelle) Einstellungen, einen schnelleren Suchlauf, den Suchlauf mit grafischer Darstellung (Spektrumanalysator-Modus) und vieles mehr. |
| 11 | Welche Firmware ist die beste? | Diejenige, die Ihren Anforderungen am besten entspricht |
| 12 | Wie sichere ich die Werks-Firmware? | Es ist sinnlos, die Werks-Firmware zu sichern, denn sie ist im Internet und auf der Website des Herstellers frei verfügbar. Weitaus wichtiger ist es, die originalen Kalibrierdaten (die für Ihr Funkgerät einzigartig sein können) und die Konfigurationsdatei zu sichern. Das geschieht mit dem Programm k5prog. |
| 13 | Der Computer erkennt das über den eingebauten Type-C-Anschluss verbundene Funkgerät nicht | Der im Funkgerät eingebaute Type-C-Anschluss ist ausschließlich zum Laden des Akkus vorgesehen.<br>Das Flashen erfolgt über ein spezielles Programmierkabel mit einem Stecker vom Typ KENWOOD. (ein Kabel von analogen Baofeng-Funkgeräten und ähnlichen Geräten ist geeignet) |
| 14 | Funktioniert ein Kabel von einem Baofeng zum Flashen und Konfigurieren? | Ja, es funktioniert (eines von analogen Funkgeräten) |
| 15 | Wie beginne ich mit dem Flashen | Jedes Flashen sollte mit einer Prüfung des Akkuladezustands beginnen. Ist der Akku auf unter 50 % (~7.2 V) entladen, kann der Flash-Vorgang fehlerhaft oder unvollständig verlaufen.<br>Zum Flashen sollten Sie ein Programmierkabel mit einem Stecker vom Typ KENWOOD kaufen oder selbst anfertigen und den Treiber für dieses Kabel auf Ihrem PC installieren. Bereiten Sie das Flash-Programm vor. Bereiten Sie die Firmware selbst vor. Verbinden Sie das eingeschaltete Funkgerät über das beschaffte Kabel mit dem PC und sichern Sie mit dem Programm Ihre eigenen Kalibrierdaten und die Konfigurationsdatei. Schließen Sie |

das Funkgerät im Flash-Modus an. Führen Sie mit dem Programm die Firmware-Datei aus.

**16. Wo finde ich eine ausführliche Flash-Anleitung?**

Siehe den Abschnitt SCHNELLANLEITUNG ZUM FLASHEN DES QUANSHENG UV-K5 UND SEINER MODIFIKATIONEN.

**17. Der Computer erkennt das Funkgerät nicht**

- Das Kabel ist nicht vollständig in das Funkgerät eingesteckt (beim ersten Einstecken geht das Kabel sehr stramm hinein, oft bis es einrastet).
- Die Kabeltreiber sind nicht installiert oder es sind die falschen Treiber installiert.

**18. Mit welchem Programm soll ich flashen?**

Modifizierte Firmware sollte wie folgt geflasht werden:
- die Versionen UV-K5, K5(8) und K5+ sollten mit k5prog-win geflasht werden — empfohlen wird Version 1.26
- die Versionen UV-K5+ (mit Type-C-Anschluss) sollten mit k5tools geflasht werden

**19. Ich habe das Funkgerät geflasht, beim Einschalten fragt es jedoch nach irgendeinem Passwort.**

Versuchen Sie alle Ziffern 000000 oder 111111 oder 123400, oder halten Sie am ausgeschalteten Funkgerät MENU+EXIT gedrückt und schalten Sie es ein, während Sie die Tasten weiterhin gedrückt halten.

Außerdem kann das Funkgerät blockieren und beim Einschalten einen Code verlangen, wenn bei der Konfiguration über CHIRP oder PSCPS die Seitentasten FN1 und/oder FN2 auf NONE (nicht belegt) gesetzt wurden.

Hilft das nicht, löschen Sie den Speicher des Funkgeräts mit der REBORN-Firmware — siehe Abschnitt 6 dieser Anleitung.

**20. Mit welchem Programm soll ich das Funkgerät programmieren (konfigurieren)?**

CHIRP oder PSCPS.

Für CHIRP müssen Sie das Modul laden.

**21. Was ist CHIRP und was kann es?**

Es ist ein Programm zum Programmieren von Funkgeräten. Es bearbeitet Kanäle und schaltet verschiedene Funktionen ein und aus, auch solche, die über das Menü des Funkgeräts selbst nicht zugänglich sind.

**22. Ich habe meine gespeicherten Frequenzen (aus einer anderen Firmware) oder die Frequenzdatei einer anderen Person geladen, und das Funkgerät verhält sich fehlerhaft**

Konfigurationsdateien aus unterschiedlichen Firmware-Versionen können dazu führen, dass das Funkgerät fehlerhaft arbeitet; deshalb wird vom Laden solcher Dateien abgeraten. Auch vom Laden fremder Konfigurations- und Einstellungsdateien wird abgeraten.

Wenn Sie Frequenzen aus einer fremden Datei (oder aus Ihrer eigenen, aber mit einer anderen Firmware erstellten Datei) schreiben müssen, verwenden Sie CHIRP: Öffnen Sie die fremde Datei, lesen Sie Ihr Funkgerät aus — es erscheint ein zweiter Tab; kopieren Sie die benötigten Frequenzen aus dem Tab der fremden Datei und fügen Sie sie in den Tab der Datei Ihres Funkgeräts ein. Vergessen Sie nicht, vor dem Einlesen von Dateien das entsprechende Modul zu laden.

**23. Verfügt das Funkgerät über eine Verschlüsselung?**

Das Funkgerät besitzt keine Signalverschlüsselung, wohl aber eine Scrambler-Funktion (Sprachverschleierung). Bitte beachten Sie, dass die Gesetzgebung

vieler Länder den Einsatz von Verschlüsselung, Scramblern und anderen Funktionen zur Signalverschleierung im zivilen Funkverkehr gesetzlich verbietet.

**24. Warum leuchtet beim Empfang die grüne LED, während der Lautsprecher stumm bleibt?**

- prüfen Sie, ob Sie Empfangs-Subtöne eingestellt haben (R-DCS und R-CTCS);
- prüfen Sie, ob beide Funkgeräte dieselbe Modulation verwenden (insbesondere FM).

**25. Was ist ein Subton?**

Ein Subton ist ein zusätzliches, für das menschliche Ohr nicht hörbares Signal, das zusammen mit der Sprache übertragen wird. Er wirkt wie eine Art "Freund-Feind"-Kennung (durch Filterung des eingehenden Signals). Wenn ein Subton eingestellt ist, weist Ihr Funkgerät jedes Signal auf dieser Frequenz ab und öffnet den Empfang nur dann, wenn es ein Signal mit demselben Subton erkennt.

Ein Funkgerät ohne Subton hört beim Empfang dagegen alle anderen Funkgeräte, sowohl die mit Subton als auch die ohne.

**26. Was ist der nicht normgerechte 55-Hz-Subton, den der Scanner erkennt?**

Siehe die Beschreibung in der Anleitung zur Karina-Firmware, Punkt 22, S. 5.

**27. Warum höre ich den einen Gesprächspartner, den anderen aber nicht?**

Das bedeutet, dass das Signal des einen Funkers stark genug ist, damit Sie ihn hören, während das Signal des zweiten zu schwach ist.

Die Ursache kann eine wenig wirksame Antenne sein, oder einer der Funker befindet sich näher bei Ihnen, oder das Signal des zweiten Funkers ist schlicht zu schwach.

Möglich ist auch der umgekehrte Fall: Das Signal eines der Gesprächspartner ist so stark, dass es Ihren Empfänger übersteuert; dieser "verschluckt" sich am übermäßig starken Signal und verstummt.

**28. Warum stelle ich das Funkgerät auf Frequenzsuchlauf und höre niemanden?**

Um jemanden zu hören, müssen Sie zunächst entscheiden, wo Sie suchen wollen. Mit dem Suchlauf "über alles auf einmal" kommen Sie nicht weiter.

Ein Beispiel: Sie wollen das Band 100–200 MHz mit einer Schrittweite von 25 kHz absuchen (die Suchlaufgeschwindigkeit im Frequenzmodus beträgt etwa 15 Frequenzen pro Sekunde), das ergibt 100/((0.025)*15) = 266 Sekunden (fast 5 Minuten) für einen Suchlaufzyklus. Weitaus wirksamer ist es, den Suchbereich einzugrenzen oder den Suchlauf im Spektrumanalysator-Modus mit den konfigurierten Presets zu starten.

**29. Kann das Funkgerät verwendet werden, um Hilfe zu rufen?**

In Ausnahmefällen und nur **wenn eine unmittelbare Gefahr für Leben und Gesundheit von Menschen besteht und es keine Möglichkeit gibt, über andere technische Kommunikationsmittel Hilfe zu rufen**, dürfen Sie einen Notruf SOS oder MAYDAY absetzen.

**30. Welche Frequenzen eignen sich am besten für einen Hilferuf, damit ich gehört werde?**

Es gibt keine allgemeingültigen Notruffrequenzen. Es gibt Seenot-, Binnenschifffahrts-,

Bergrettungsfrequenzen und so weiter. Diese Frequenzen können sich zudem je nach Region und Land unterscheiden. Wenn Sie eine Reise in eine bestimmte Region planen, sollten Sie sich zumindest erkundigen, welche Notfunkfrequenzen dort verwendet werden.

Es gibt jedoch allgemein anerkannte Anruffrequenzen, auf denen Sie eher gehört werden:

433.500 — die allgemeine Anruffrequenz des 70-cm-Bandes
446.09375 — die allgemeine Anruffrequenz des PMR-Bandes
145.500 — die allgemeine Anruffrequenz für Funkamateure (für die Verbindung zwischen Funkamateuren, die über Lizenzen und Genehmigungen verfügen)

Je nach Region können auch diese Frequenzen abweichen.

Es wird davon abgeraten, diese Frequenzen mit langen Gesprächen zu belegen. Sie können auf ihnen jederzeit Kontakt aufnehmen und danach nach Absprache auf andere Frequenzen wechseln.

**31. Was bedeutet das Symbol S, das von Zeit zu Zeit oben links aufleuchtet?**

Siehe die Beschreibung in der Anleitung zur Karina-Firmware, Punkt 14, S. 5.

**32. Warum werden die Änderungen nicht gespeichert, wenn ich die Sendeleistung (oder die Bandbreite, die Modulation, den Subton oder den Frequenzversatz) ändere und danach auf einen anderen Kanal und zurück wechsle oder das Funkgerät aus- und wieder einschalte?**

Siehe die Beschreibung in der Anleitung zur Karina-Firmware, Punkt 13, S. 5.

**33. Beim Drücken der PTT-Taste wird DISABLE angezeigt — was soll ich tun?**

Siehe die Beschreibung in der Anleitung zur Karina-Firmware, Punkte 36 und 37, S. 7.

**34. Ich habe ein Type-C-Kabel an das Funkgerät angeschlossen, es lädt aber nicht**

Das Laden über Type-C ist eine zusätzliche Option. Es beginnt erst bei einer niedrigeren Akkuspannung und lädt den Akku nicht bis zu seinem Nennwert auf. Wann immer das Laden über die Ladeschale möglich ist, verwenden Sie die Ladeschale.

**35. Meine Akkuspannung wird falsch angezeigt — was soll ich tun?**

Wenn die auf dem Display des Funkgeräts angezeigte Akkuspannung unglaubwürdig niedrig (~0.25 V) oder unglaubwürdig hoch (600 V) ist, so ist das das erste Anzeichen dafür, dass Ihre Kalibrierungen beschädigt sind: Sie müssen zuerst die Werkskalibrierungen und erst danach die Karina-Kalibrierungen laden. Hilft das nicht, löschen Sie den Speicher wie in der Firmware-Anleitung beschrieben und installieren Sie anschließend die Firmware und die Kalibrierungen erneut.

Wird die Spannung mehr oder weniger korrekt angezeigt, mit einer Abweichung von etwa 0.2–0.5 V gegenüber dem mit einem Multimeter gemessenen Wert, so ist das bei den Werkskalibrierungen der Normalfall. Das lässt sich mit einem HEX-Editor korrigieren, indem Sie den Wert der Zelle 140/6 der Kalibrierdatei ändern (bei mir ist dieser Wert =B0, bei Ihnen kann er abweichen).

**36. Warum werden 6.0 V angezeigt, während sich das Funkgerät bereits abschaltet?**

Der Betriebsspannungsbereich des Akkus liegt bei ~6.0 V – 8.4 V

~8.4 V = 100%
~7.2 V = 50%
~6.0 V = 0%

Eine Entladung des Akkus unter 4 V führt zu seiner Degradation.
