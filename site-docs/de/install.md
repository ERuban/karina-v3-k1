## FLASHEN der Funkgeräte Quansheng UV-K5V3 und K1

### und Arbeiten mit CHIRP

**BEVOR SIE ÜBERHAUPT IRGENDETWAS TUN:**

**1.**
**Vergewissern Sie sich, dass Sie eine Version K1 oder K5V3 besitzen!!!**

**Die Version V1 trägt keine Kennzeichnung.**
**Die Versionen V2 und V3 tragen die entsprechende Kennzeichnung üblicherweise auf dem Etikett**
**unter dem Akku.**

![screenshot](images/p01_3.png)

![screenshot](images/p01_1.png)

**Die Firmware ist zwischen den Versionen NICHT austauschbar. Wenn Sie versuchen, ein Funkgerät**
**mit einer Firmware für eine andere Version zu flashen, erhalten Sie ein unbrauchbares (gebricktes) Funkgerät.**

Versionen V1 haben einen Bootloader, der mit 2, 3, 4 oder 5 beginnt
Versionen V2 haben einen Bootloader, der mit 1 beginnt
Versionen V3 haben einen Bootloader, der mit 7 beginnt

Sie können dies in k5prog-win überprüfen, wenn das Funkgerät im Flash-Modus angeschlossen ist:

![screenshot](images/p01_2.png)

**Erstellen Sie ein BACKUP der werkseitigen Kalibrierungen**

**INHALT:**

**1. EIN KURZER ÜBERBLICK ÜBER DIE INSTALLATION DER FIRMWARE KARINA (Autumn rain)**
**auf den Funkgeräten Quansheng UV-K5(V3) und UV-K1.**

**2. Die ausführliche Anleitung zur Firmware-Installation.**

**3. VERWENDUNG VON CHIRP.**
3.1. Herunterladen des Moduls
3.2. Verwendung des Moduls mit CHIRP (Karina)
3.3. Kopieren von Frequenzen aus einer fremden Datei.

**4. HÄUFIG GESTELLTE FRAGEN, MÖGLICHE PROBLEME UND IHRE LÖSUNG.**

## 1. EIN KURZER ÜBERBLICK ÜBER DIE INSTALLATION DER FIRMWARE KARINA (Autumn rain)

**auf den Funkgeräten Quansheng UV-K5(V3) und UV-K1:**

**Diese Anleitung gilt ausschließlich für das Flashen des K5(V3) oder des K1.**
**Der Versuch, Firmware für das K5V3 (oder K1) in ein K5V1 zu laden = ein gebricktes Funkgerät.**

**Wenn Sie bereits Erfahrung mit dem Flashen haben, ist diese Kurzanleitung für Sie.**
**Falls nicht, folgt weiter unten eine ausführlichere Anleitung mit Erläuterungen und Bildern.**

**Laden Sie vor dem Flashen den AKKU VOLLSTÄNDIG AUF.**

**EIN KURZER ÜBERBLICK ÜBER BACKUP UND FLASHEN**

**1.** Schalten Sie das Funkgerät ein und schließen Sie es über USB Type-C (oder mit einem Kenwood-Kabel) an.

**2.** Erstellen Sie ein Backup der werkseitigen Kalibrierungen und der Konfiguration.

**3.** Schalten Sie das Funkgerät aus und anschließend wieder ein, während Sie die Taste PTT gedrückt halten.

**4.** Installieren Sie die Firmware mit dem Flash-Programm Ihrer Wahl
(die Datei mit dem Index `packed` – für das werkseitige Flash-Programm **qpscps** / die Datei OHNE den
Index `packed` – für jedes andere Flash-Programm).

**5.** **TRENNEN SIE DAS KABEL VOM COMPUTER!!!** Schalten Sie das Funkgerät aus und anschließend wieder ein, während Sie
**PTT+EXIT** gedrückt halten (etwa 2 Sekunden halten) – der Speicher wird gelöscht.

**6.** Öffnen Sie das Flash-Programm erneut und schreiben Sie die werkseitigen Kalibrierungen zurück.

**7.** Schreiben Sie die Kalibrierungen, die mit der Firmware **Karina** mitgeliefert werden.

**8.** Schreiben Sie die Konfiguration zurück (falls erforderlich).
Alternativ richten Sie alles von Hand über das Menü des Funkgeräts oder über CHIRP ein
*(nur Konfigurationen aus früheren Versionen funktionieren; Konfigurationsdateien anderer*
*Firmware*
*funktionieren nicht).*

**ACHTUNG!!!**
**Wenn Sie die 3 Presets separat konfigurieren (siehe Punkt 35 des Einstellungsmenüs), müssen Sie**
**die Schritte 5-8 für jedes einzeln ausführen und zuvor jeweils das benötigte Preset in Punkt 35**
**auswählen. !!!**

**Zur Erinnerung:**

**Kalibrierungen und Konfiguration werden gelesen und geschrieben**, während das Funkgerät im
Normalmodus eingeschaltet ist.

**Das Flashen** erfolgt bei einem im Flash-Modus eingeschalteten Funkgerät (bei ausgeschaltetem Gerät PTT gedrückt halten und
das Funkgerät einschalten, ohne die Taste loszulassen). Das Display bleibt dunkel, und die Taschenlampen-LED
leuchtet auf und zeigt damit an, dass sich das Funkgerät im Flash-Modus befindet.

## 2. DIE AUSFÜHRLICHE ANLEITUNG ZUR FIRMWARE-INSTALLATION

**Laden Sie vor dem Flashen den AKKU VOLLSTÄNDIG AUF.**

**1.** Schalten Sie das Funkgerät ein und schließen Sie es über USB Type-C (oder mit einem Kenwood-Kabel) an.

**!!! Funkgeräte Quansheng UV-K1, die für den chinesischen Markt gefertigt wurden,** haben Probleme mit der
Verbindung über USB Type-C; verwenden Sie mit ihnen besser ein Kenwood-Kabel.

![screenshot](images/p03_1.png)

Version für den europäischen Markt

Version
für den
chinesischen
Markt

**2.** **ERSTELLEN SIE EIN BACKUP DER KALIBRIERUNGEN UND DER KONFIGURATION**

Öffnen Sie dazu **k5prog-win** (empfohlen wird Version v0.1.26) und erstellen Sie das
Backup:

Kalibrierungen: Drücken Sie **read calibration** und speichern Sie die werkseitigen Kalibrierungen.
Konfiguration: Drücken Sie **read configuration** und speichern Sie die werkseitige Konfiguration.

![screenshot](images/p03_2.png)

**3.** Schalten Sie das Funkgerät aus und anschließend wieder ein, während Sie die Taste PTT gedrückt halten.

**4.** Öffnen Sie das Originalprogramm **qpscps** ( https://en.qsfj.com/support/downloads/8740 ),
wählen Sie den COM-Port und das Flash-Menü (alt+D, der dritte Eintrag).

![screenshot](images/p04_1.png)

Geben Sie den Pfad zur Datei **packed** an und flashen Sie das Funkgerät durch Drücken von **Update**.

![screenshot](images/p04_2.png)

*(Wenn Sie online über die Seite https://armel.github.io/uvtools2/ flashen, drücken Sie auf dem Reiter* ***Flash***
***Firmware*** *die Schaltfläche* ***Choose file*** *und wählen Sie die Firmware ohne den Index* ***packed****,*

![screenshot](images/p04_4.png)

![screenshot](images/p04_3.png)

*drücken Sie* ***Flash firmware****, wählen Sie den* ***COM port*** *und flashen Sie das Funkgerät.)*

**5.** **TRENNEN SIE DAS KABEL VOM COMPUTER!!!** Schalten Sie das Funkgerät aus und anschließend wieder ein, während Sie
**PTT+EXIT** etwa 2 Sekunden lang gedrückt halten – der Speicher wird gelöscht.

**6.** Öffnen Sie **k5prog-win** erneut und schreiben Sie die werkseitigen Kalibrierungen mit der Schaltfläche
**Write calibration** zurück.

![screenshot](images/p05_1.png)

*(Dies ist auch über die Seite https://armel.github.io/uvtools2/ möglich (wenn Sie die Kalibrierungen*
*mit* ***k5prog-win*** *gespeichert haben, müssen Sie die Dateiendung von* ***bin*** *in* ***dat*** *ändern). Wählen Sie dazu auf dem Reiter*
***Restore Calib*** *die benötigte Datei über die Schaltfläche* ***Choose file****, drücken Sie* ***Restore***
***Calibration Data****, wählen Sie den* ***COM port*** *und schreiben Sie die Kalibrierungen.)*

![screenshot](images/p05_3.png)

![screenshot](images/p05_2.png)

**7.** Schreiben Sie die Kalibrierungen ein weiteres Mal, diesmal mit den Karina-Kalibrierungen (zum Zeitpunkt der
Erstellung dieser Anleitung ist das **calib5**) – nach demselben Verfahren wie in Schritt 6.

**8.** Schreiben Sie die Konfiguration mit **k5prog-win** und der Schaltfläche **Write configuration** zurück.
*(Nur Konfigurationen aus früheren Versionen funktionieren; Konfigurationsdateien anderer Firmware*
*funktionieren nicht.)*

![screenshot](images/p05_4.png)

## WENN SIE VON DER FIRMWARE KARINA WEGWECHSELN MÜSSEN

(weil sich ihre Speicheraufteilung von der anderer Firmware unterscheidet)
müssen Sie Folgendes tun:

**1. Löschen Sie den Speicher** (Funkgerät ausschalten, dann wieder einschalten und dabei die Tasten PTT+EXIT gedrückt halten (etwa 2 Sekunden halten))

**2. Installieren Sie eine beliebige andere MOD-FIRMWARE** (die Werksfirmware eignet sich nicht, da sie das Schreiben von Kalibrierungsdaten nicht zulässt)

**3. Schreiben Sie Ihre ursprünglichen werkseitigen Kalibrierungsdaten zurück.**

**4. Nutzen Sie das Funkgerät** oder installieren Sie nach Belieben etwas anderes (auch die Werksfirmware).

## 3. VERWENDUNG VON CHIRP

### 3.1. Laden des Moduls

**WICHTIG!!!** Derzeit gibt es kein eigenes CHIRP-Modul für die Firmware Karina. Es existieren Module, die für andere Firmware geschrieben wurden und mehr oder weniger mit Karina kompatibel sind. Das unten genannte Modul wurde ursprünglich für die Firmware F4 geschrieben und stellenweise an Karina angepasst. Dennoch sollten Sie nicht alles Erdenkliche über CHIRP verändern, da die Kompatibilität nicht vollständig ist.

Bei der Verwendung von CHIRP müssen Sie ein Modul in das Programm laden (*für Karina verwenden Sie das Modul aus dem Archiv*; **für andere Firmware müssen Sie das jeweils passende Modul wählen**). Starten Sie dazu CHIRP, klicken Sie auf "HELP" und aktivieren Sie den Entwicklermodus. Starten Sie anschließend CHIRP neu, öffnen Sie das Menü "File", wählen Sie "Load module" und wählen Sie die Datei aus dem Archiv aus.

![screenshot](images/p07_1.png)

![screenshot](images/p07_2.png)

**!!! WICHTIG:** Das Modul wird beim Schließen von CHIRP entladen und muss daher bei jedem Start von CHIRP erneut geladen werden.

**Weiter:** Radio -> Download from radio -> COM-Port auswählen -> Vendor (Quansheng) -> im Feld Model das Modul für Ihre Firmware.

![screenshot](images/p07_4.png)

![screenshot](images/p07_3.png)

### 3.2. Verwendung des Moduls mit CHIRP (Karina)

Wie oben erwähnt, ist es nicht ratsam, jede Funktion in CHIRP zu verändern, da das Modul nicht vollständig kompatibel ist. Nachfolgend ein Beispiel dafür, was gefahrlos bearbeitet werden kann (**grün markiert**) und wovon dringend abgeraten wird (**rot markiert**):

**Auf dem ersten Reiter** mit den Speicherkanälen kann alles gefahrlos bearbeitet werden.

**Auf dem zweiten Reiter, Basic Settings**, können Sie die folgenden Funktionen frei ändern (alle außer der Begrüßungsmeldung lassen sich auch über das Menü des Funkgeräts ändern):

![screenshot](images/p08_1.png)

**Auf dem zweiten Reiter, Programmable Keys**, können Sie die Einstellungen der seitlichen Tasten FN1 und FN2 ändern. Diese Einstellungen lassen sich nur über die Software ändern, nicht über das Menü des Funkgeräts:

![screenshot](images/p08_2.png)

Achten Sie darauf, dass den seitlichen Tasten sowohl für kurzes als auch für langes Drücken Werte zugewiesen sind (wenn NONE eingestellt ist, blockiert das Funkgerät und fragt nach einem Code!).

**Auf dem zweiten Reiter, ScanList**, können Sie die Standard-Suchliste festlegen und die Prioritätskanäle für das Scannen in den Suchlisten 1 und 2 auswählen (diese Einstellungen sind sowohl in CHIRP als auch im Menü des Funkgeräts verfügbar):

![screenshot](images/p09_1.png)

**Auf dem zweiten Reiter, Unlock Settings**, können Sie die Sendesperre für den Frequenzplan auswählen (diese Einstellungen sind sowohl in CHIRP als auch im versteckten Menü des Funkgeräts verfügbar):

![screenshot](images/p09_2.png)

**Auf dem zweiten Reiter, FM Broadcast Receiver**, können Sie die im Speicher abgelegten Frequenzen der UKW-Rundfunksender zuweisen (diese Einstellungen sind sowohl in CHIRP als auch im versteckten Menü des Funkgeräts verfügbar):

![screenshot](images/p09_3.png)

### 3.3. Kopieren von Frequenzen aus einer fremden Datei

Es ist nicht ratsam, eine fremde Frequenzdatei oder eine Datei aus einer anderen Firmware in Ihr Funkgerät zu laden. CHIRP und PSCPS laden im Wesentlichen eine Konfiguration (die Einstellungen des Funkgeräts), und deren Struktur kann sich zwischen Firmware-Versionen unterscheiden (und sogar zwischen verschiedenen Releases der Firmware desselben Entwicklers).

Das Laden einer solchen fremden Konfigurationsdatei kann das Funkgerät instabil machen (kein Empfang, schlechter Empfang, Probleme beim Senden oder mit der Modulation und so weiter).

**Wenn Sie Frequenzen aus einer fremden Datei in ein Funkgerät mit Karina kopieren müssen, gehen Sie**
**folgendermaßen vor:**

- Öffnen Sie sie in CHIRP (laden Sie zuvor, falls nötig, das erforderliche Modul — die Module können sich von Firmware zu Firmware unterscheiden)
- Laden Sie das Modul für Karina
- Schließen Sie das Funkgerät an den Computer an und wählen Sie Radio -> Download From Radio; wählen Sie im sich öffnenden Menü den Port, den Hersteller des Funkgeräts und das benötigte Modul aus

![screenshot](images/p10_1.png)

![screenshot](images/p10_2.png)

Danach haben Sie zwei Reiter geöffnet: die "Spender"-Datei und Ihr eigenes Funkgerät.

- Wählen Sie auf dem Reiter der "Spender"-Datei die benötigten Frequenzen aus und wählen Sie Copy; wechseln Sie dann auf den Reiter Ihres eigenen Funkgeräts, markieren Sie die erste Zeile, ab der Sie beginnen möchten, und fügen Sie die Frequenzen ein. *(unten ein Beispiel für das Kopieren von Daten zwischen zwei zueinander inkompatiblen Funkgeräten, einem Baofeng und einem Quansheng)* - **diese Art des Kopierens ist sicher, denn dabei werden nur die Kanäle (deren Frequenzen, Namen und Einstellungen) kopiert, die allgemeinen Einstellungen des Funkgeräts bleiben unberührt**

![screenshot](images/p10_4.png)

![screenshot](images/p10_3.png)

## 4. HÄUFIG GESTELLTE FRAGEN, MÖGLICHE PROBLEME UND LÖSUNGEN

**Probleme und Fragen — mögliche Lösungen, Anmerkungen und Antworten.**

### Nach Installation und Konfiguration der Firmware lässt sich im VFO-Modus keine Frequenz eingeben

Bei der Installation der Firmware MUSS das Kabel vom Computer getrennt werden, bevor Sie das Löschen des Speichers mit PTT+EXIT durchführen. Sie müssen den Löschvorgang erneut ausführen, danach die Kalibrierungsdaten schreiben und das Funkgerät konfigurieren.

### 1. Auf welchen Frequenzen darf ich senden?

Es gibt zivile Funkfrequenzen, die für die lizenzfreie Nutzung freigegeben sind. In der Regel sind dies:

- CB (25.165 – 29.445 MHz) mit einer Sendeleistung von 4,0-12,0 W
- LPD (433.075 – 434.775 MHz) mit einer Sendeleistung von 0,01 W
- PMR (446.00625 – 446.19375) mit einer Sendeleistung von 0,5 W

In einigen Ländern werden außerdem die Bänder FRS und GMRS genutzt.

### 2. Auf welchen Frequenzen darf ich nicht senden?

Ohne Sondergenehmigung ist das Senden außerhalb der zivilen Bänder gesetzlich verboten. Alle übrigen Frequenzbereiche werden von anderen Diensten genutzt, von Funkamateuren bis zu Behörden, einschließlich Satelliten, Mobilfunknetzen, Fluglotsen und Luftfahrzeugen, Wetterstationen, Binnen- und Seefunk, Militär und anderen. Wenn Sie den Betrieb eines dieser Dienste stören, können Sie nach den Gesetzen Ihres Landes zur Verantwortung gezogen werden.

### 3. Auf welchen Frequenzen empfängt und sendet das Quansheng UV-K5?

In der Firmware Karina sind Empfang und Senden auf allen Bändern freigeschaltet (siehe Abschnitt 2.2, Betriebsfrequenzbänder).

Bei Funkgeräten ohne Hardware-Modifikation ist das Senden ohne das Risiko, das Gerät zu zerstören, nur innerhalb der vom Hersteller angegebenen Bänder zulässig: 136-174 MHz / 400-470 MHz.

### 4. Was passiert, wenn ich ohne Antenne sende?

Das Senden ohne Antenne, ebenso wie mit einer auf ein anderes Frequenzband abgestimmten Antenne, zerstört die Endstufe des Funkgeräts.

### 5. Sendet das Funkgerät im CB-Band? Kann ich mit Lkw-Fahrern sprechen?

In der Firmware Karina ist das 27-MHz-Band standardmäßig sowohl für den Empfang als auch für das Senden freigeschaltet.

Für den Empfang benötigen Sie eine auf dieses Band abgestimmte Antenne.

Das Senden in diesem Band mit einem hardwareseitig nicht modifizierten Funkgerät ergibt jedoch keine brauchbare Verbindung (die Ausgangsleistung ist viel zu gering). Zugleich erzeugt ein Sendeversuch in diesem Band aufgrund der physikalischen Eigenschaften des Funkgeräts Störungen im Flugfunkband und zerstört außerdem die Endstufe des Funkgeräts.

### 6. Warum hört mich im CB-Band niemand?

Im Werkszustand überschreitet die Sendeleistung des Funkgeräts im CB-Band 0,01 W nicht. Folglich ist das Senden in diesem Band ohne physische Modifikation nicht nur nutzlos, sondern auch gefährlich für das Funkgerät selbst.

### 7. Warum ist die Verbindung im Auto schlecht?

Die Karosserie schirmt Funksignale ab. Für eine stabile Verbindung wird empfohlen, eine Außenantenne außerhalb der Karosserie zu montieren.

### 8. Warum sollte ich das Funkgerät überhaupt flashen?

Ein serienmäßiges Funkgerät funktioniert ab Werk zuverlässig und erfüllt seine Aufgaben.

Modifizierte Firmware erweitert den Funktionsumfang des Funkgeräts und bietet zusätzliche und flexiblere (professionelle) Einstellungen, eine höhere Suchlaufgeschwindigkeit, das Scannen mit grafischer Anzeige (Spektrumanalysator-Modus) und so weiter.

### 9. Welche Firmware ist die beste?

Diejenige, die Ihren Anforderungen am besten entspricht.

### 10. Wie sichere ich die Werksfirmware?

Es hat keinen Sinn, die Werksfirmware zu sichern, da sie im Internet und auf der Website des Herstellers frei verfügbar ist. Weitaus wichtiger ist es, die originalen Kalibrierungsdaten (die für Ihr Gerät einzigartig sein können) und die Konfigurationsdatei zu sichern. Dies geschieht mit dem Programm k5prog.

### 11. Der Computer erkennt das Funkgerät nicht, wenn es über den eingebauten Type-C-Anschluss verbunden ist

Der im Funkgerät eingebaute Type-C-Anschluss ist ausschließlich zum Laden des Akkus vorgesehen.

Das Flashen erfolgt mit einem speziellen Programmierkabel mit einem Stecker vom Typ KENWOOD (ein Kabel von analogen Baofeng-Funkgeräten und ähnlichen Geräten ist geeignet).

### 12. Funktioniert ein Baofeng-Kabel zum Flashen und Programmieren?

Ja, es funktioniert (eines von analogen Funkgeräten).

### 13. Womit beginne ich das Flashen?

Jedes Flashen sollte mit einer Prüfung des Akkuladestands beginnen. Wenn der Akku unter 50 % (~7,2 V) geladen ist, kann der Flash-Vorgang fehlerhaft oder unvollständig verlaufen.

Zum Flashen müssen Sie ein Flash-Kabel mit einem Stecker vom Typ Kenwood kaufen oder anfertigen und den Treiber für dieses Kabel auf dem PC installieren.

Bereiten Sie das Flash-Programm vor. Bereiten Sie die Firmware-Datei selbst vor. Schließen Sie das eingeschaltete Funkgerät mit dem erworbenen Kabel an den PC an und erstellen Sie mit dem Programm ein Backup Ihrer Kalibrierungsdaten und der Konfigurationsdatei. Schließen Sie das Funkgerät anschließend im Flash-Modus an und schreiben Sie mit dem Programm die Firmware-Datei.

### 14. Wo finde ich eine ausführliche Flash-Anleitung?

Siehe den Abschnitt KURZANLEITUNG ZUM FLASHEN DES QUANSHENG UV-K5 UND SEINER VARIANTEN.

### 15. Der Computer erkennt das Funkgerät nicht

- Das Kabel ist nicht vollständig in das Funkgerät eingesteckt (beim ersten Mal geht es sehr stramm hinein, oft bis es hörbar einrastet).
- Der Treiber für das Kabel ist nicht installiert oder es ist der falsche Treiber installiert.

### 16. Welches Programm soll ich zum Flashen verwenden?

Modifizierte Firmware sollte folgendermaßen geflasht werden:

- die Versionen UV-K5, K5(8) und K5+ sollten mit k5prog-win geflasht werden — empfohlen wird Version 1.26;
- die Version UV-K5+ (mit Type-C-Anschluss) sollte mit k5tools geflasht werden.

### 17. Ich habe das Funkgerät geflasht, aber beim Einschalten fragt es nach einem Passwort

Probieren Sie lauter gleiche Ziffern — 000000 oder 111111 — oder 123400, oder halten Sie am ausgeschalteten Funkgerät MENU+EXIT gedrückt und schalten Sie es ein, ohne die Tasten loszulassen.

Außerdem kann das Funkgerät blockieren und beim Einschalten nach einem Code fragen, wenn Sie bei der Konfiguration über CHIRP oder PSCPS die seitlichen Tasten FN1 und/oder FN2 auf NONE (nicht zugewiesen) gesetzt haben.

Wenn das nicht hilft, löschen Sie den Speicher des Funkgeräts mit der Firmware REBORN — siehe Abschnitt 6 dieser Anleitung.

### 18. Welches Programm soll ich zum Programmieren (Konfigurieren) des Funkgeräts verwenden?

CHIRP oder PSCPS. Für die Verwendung von CHIRP müssen Sie das Modul laden.

### 19. Was ist CHIRP und was kann es?

Es ist ein Programm zum Programmieren von Funkgeräten. Es bearbeitet Kanäle und schaltet verschiedene Funktionen ein und aus, darunter auch solche, die über das Menü des Funkgeräts selbst nicht verfügbar sind.

### 20. Ich habe meine gespeicherten Frequenzen (aus einer anderen Firmware) oder eine fremde Frequenzdatei geschrieben, und das Funkgerät verhält sich seltsam

Konfigurationsdateien aus anderen Firmware-Versionen können dazu führen, dass das Funkgerät nicht korrekt arbeitet; deshalb wird vom Schreiben solcher Dateien abgeraten. Auch das Schreiben fremder Konfigurations- und Einstellungsdateien wird nicht empfohlen.

Wenn Sie Frequenzen aus einer fremden Datei (oder aus Ihrer eigenen Datei, die jedoch mit einer anderen Firmware erstellt wurde) schreiben müssen, verwenden Sie CHIRP: Öffnen Sie die fremde Datei, lesen Sie Ihr Funkgerät aus — es erscheint ein zweiter Reiter — kopieren Sie dann die benötigten Frequenzen vom Reiter der fremden Datei und fügen Sie sie im Reiter Ihres Funkgeräts ein. Vergessen Sie nicht, vor dem Auslesen der Dateien das passende Modul zu laden.

### 21. Verfügt das Funkgerät über eine Verschlüsselung?

Das Funkgerät besitzt keine Signalverschlüsselung, wohl aber eine Scrambler-Funktion (Sprachverschleierung). Bitte beachten Sie, dass in vielen Ländern der Einsatz von Verschlüsselung, Scramblern und anderen signalverschleiernden Funktionen im zivilen Funkverkehr gesetzlich verboten ist.

### 22. Warum leuchtet beim Empfang die grüne LED, während der Lautsprecher stumm bleibt?

- Prüfen Sie, ob Sie Empfangs-Subtöne eingestellt haben (R-DCS und R-CTCS);
- prüfen Sie, ob beide Funkgeräte dieselbe Modulation verwenden (insbesondere FM).

### 23. Was ist ein Subton?

Ein Subton ist ein zusätzliches, für das menschliche Ohr nicht hörbares Signal, das zusammen mit der Sprache übertragen wird. Er wirkt als eine Art Freund-Feind-Kennung (durch Filterung des eingehenden Signals). Wenn ein Subton eingestellt ist, weist Ihr Funkgerät alle Signale auf dieser Frequenz zurück und öffnet den Empfang nur, wenn es ein Signal mit demselben Subton erkennt.

Ein Funkgerät ohne Subton hingegen hört beim Empfang alle anderen Funkgeräte, sowohl solche mit Subton als auch solche ohne.

### 24. Was ist der nicht standardmäßige 55-Hz-Subton, den der Scanner erkennt?

Siehe die Beschreibung im Handbuch der Firmware Karina, Punkt 22, Seite 5.

### 25. Warum höre ich den einen Gesprächspartner, den anderen aber nicht?

Das bedeutet, dass das Signal des einen Funkers stark genug ist, damit Sie ihn hören, während das Signal des anderen zu schwach ist.

Das kann daran liegen, dass Ihre Antenne nicht sehr leistungsfähig ist, oder daran, dass sich einer der Funker näher bei Ihnen befindet, oder schlicht daran, dass das Signal des zweiten Funkers zu schwach ist.

Auch der umgekehrte Fall ist möglich: Das Signal eines der Gesprächspartner ist so stark, dass es Ihren Empfänger übersteuert, der dann an dem übermäßig starken Signal "erstickt" und stumm bleibt.

### 26. Ich habe das Funkgerät auf Frequenzsuchlauf gestellt — warum höre ich niemanden?

Um jemanden zu hören, müssen Sie zunächst entscheiden, wo Sie suchen wollen. Mit dem Scannen von "allem auf einmal" kommen Sie nicht weiter.

Angenommen, Sie wollen den Bereich 100-200 MHz mit einer Schrittweite von 25 kHz absuchen (die Suchlaufgeschwindigkeit im Frequenzmodus (VFO) beträgt etwa 15 Frequenzen pro Sekunde), dann ergibt das:

100/((0,025)*15)=266 Sekunden (also fast 5 Minuten) für einen einzigen Suchlaufdurchgang. Weitaus effizienter ist es, den Suchbereich einzugrenzen oder den Suchlauf im Spektrumanalysator-Modus unter Verwendung der konfigurierten Presets zu starten.

### 27. Darf ich mit dem Funkgerät einen Hilferuf absetzen?

In Ausnahmefällen und nur, **wenn eine unmittelbare Gefahr für Leben und Gesundheit von Menschen besteht und es keine Möglichkeit gibt, über andere technische Kommunikationsmittel Hilfe zu rufen**, dürfen Sie einen Notruf SOS oder MAYDAY absetzen.

### 28. Auf welchen Frequenzen rufe ich am besten um Hilfe, damit ich gehört werde?

Es gibt keine allgemein gültigen Notfrequenzen. Es gibt Seefunkfrequenzen, Binnenschifffahrtsfrequenzen, Bergnotfrequenzen und so weiter. Diese Frequenzen können sich zudem von Region zu Region und von Land zu Land unterscheiden. Wenn Sie eine Reise in eine bestimmte Region planen, ist es ratsam, zumindest in Erfahrung zu bringen, welche Notruffrequenzen dort verwendet werden.

Es gibt jedoch allgemein gebräuchliche Anruffrequenzen, auf denen Sie eine bessere Chance haben, gehört zu werden:

- 433.500 — die allgemeine Anruffrequenz des 70-cm-Bandes
- 446.09375 — die allgemeine Anruffrequenz des PMR-Bandes
- 145.500 — die allgemeine Anruffrequenz der Funkamateure (für den Verkehr zwischen Funkamateuren mit Lizenz und Genehmigung)

Auch diese Frequenzen können sich je nach Region unterscheiden. Es wird nicht empfohlen, sie mit langen Gesprächen zu belegen. Sie können jederzeit Kontakt aufnehmen und dann nach Absprache auf andere Frequenzen wechseln.

### 29. Was bedeutet das Symbol S, das von Zeit zu Zeit oben links aufleuchtet?

Siehe die Beschreibung im Handbuch der Firmware Karina, Punkt 14, Seite 5.

### 30. Warum werden Änderungen der Sendeleistung (oder der Bandbreite, der Modulation, des Subtons oder der Frequenzablage) nicht gespeichert, nachdem ich auf einen anderen Kanal und zurück gewechselt oder das Funkgerät aus- und wieder eingeschaltet habe?

Siehe die Beschreibung im Handbuch der Firmware Karina, Punkt 13, Seite 5.

### 31. Beim Drücken von PTT zeigt das Display DISABLE an — was soll ich tun?

Siehe die Beschreibung im Handbuch der Firmware Karina, Punkte 36 und 37, Seite 7.

### 32. Ich habe ein Type-C-Kabel an das Funkgerät angeschlossen, aber es lädt nicht

Das Laden über Type-C ist eine zusätzliche Option. Es beginnt bei einer niedrigeren Akkuspannung und lädt den Akku nicht bis zu seinem Nennwert auf. Wenn Sie das Funkgerät in der Ladeschale laden können, verwenden Sie die Ladeschale.

### 33. Mein Funkgerät zeigt die Akkuspannung falsch an — was soll ich tun?

Wenn die Akkuspannung im Display des Funkgeräts unglaubwürdig niedrig (~0,25 V) oder unglaubwürdig hoch (600 V) ist, ist das das erste Anzeichen dafür, dass Ihre Kalibrierungsdaten beschädigt sind: Sie müssen zuerst die Werkskalibrierung und erst danach die Karina-Kalibrierung schreiben.

Wenn das nicht hilft, führen Sie das Löschen des Speichers wie im Firmware-Handbuch beschrieben durch und installieren Sie anschließend die Firmware und die Kalibrierungsdaten erneut.

Wird die Spannung einigermaßen korrekt angezeigt, mit einer Abweichung von etwa 0,2-0,5 V gegenüber dem mit einem Multimeter gemessenen Wert, so ist das bei der werkseitigen Kalibrierung normal. Dies lässt sich in einem HEX-Editor korrigieren, indem Sie den Wert der Zelle 140/6 der Kalibrierungsdatei ändern (in meinem Fall ist dieser Wert B0, bei Ihnen kann er abweichen).

### 34. Warum zeigt das Display 6,0 V an, während sich das Funkgerät bereits abschaltet?

Der Betriebsspannungsbereich des Akkus liegt bei ~6,0 V - 8,4 V:

- ~8,4 V = 100 %
- ~7,2 V = 50 %
- ~6,0 V = 0 %

Eine Entladung des Akkus unter 4 V führt zu seiner Degradation.
