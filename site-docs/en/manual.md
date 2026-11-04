**So, you broke it?**
**High time to open the manual.**

*Karina (autumn rain) — QUANSHENG UV-K5 (V3), UV-K1, UV-K1(8)*

![screenshot](images/p01_2.png)
![screenshot](images/p01_1.png)
![screenshot](images/p01_3.png)

## KARINA (autumn rain) firmware — description

**Version 21.08.2026**

**(version number = release day.month)**
==**Additions, clarifications and new features are marked with colour**==

 **!!! SAVE YOUR STOCK CALIBRATION DATA !!!**
**after flashing, the calibration must be updated**

**and then a reset must be performed: menu -> reset -> vfo**

## CONTENTS:

**1. MAIN SCREEN**

**2. MENU**
2.1. Menu navigation
2.2. Working frequency bands (BANDS)
==2.3. Main menu==
==2.4. Hidden menu==

**3. KEY FUNCTIONS**
==3.1. Service key combinations.==
==3.2 Front keys==
3.3. Side keys
3.4. Entering a frequency on the main screen
==3.5. Scanning in VFO and MR modes==

**4. SPECTRUM ANALYSER**
4.1. Basic spectrum mode
4.2. Additional function keys in spectrum analyser mode
4.3. Spectrum analyser settings
4.3.1. Working in "free entry" mode
4.3.2. Editing presets
4.3.3. Setting the additional spectrum analyser parameters
4.4. Active frequency capture mode — "detailed view"
4.5. Registers of the active frequency capture mode
4.6. Key assignments in the spectrum analyser modes

==**5. FREQUENTLY ASKED QUESTIONS, POSSIBLE PROBLEMS,**==
==**AND HOW TO SOLVE THEM.**==

## 1. MAIN SCREEN.

![screenshot](images/p03_1.png)

![screenshot](images/p03_2.png)

**1.**
Status line / the following symbols may be displayed:

**S** – battery saver is enabled – see section 2, item 14;
**L** – keypad is locked (Lock) – see section 3, item F (long F);
**F** - switch to the option mode – see section 3, item F (short F);
**DW** – dual watch mode – see section 2, item 17;
**A** - automatic setting of the subtone of the last reception – see section 3, item 0 (F + very long 0);
**D** - dynamic volume – see section 3, item 9 (long 9);
**r** - frequency and TX power randomiser – see section 3, item 8 (F + very long 8);
**RXTX** – automatic beacon – see section 3, items 1, 2, 3;
**x** - background frequency capture – see section 3, item 1 (long 1);
*While a signal with a subtone is being received, the status line shows the*
*analogue CTCSS tone (as a number) or the digital DCS code (in the form D125)*

**2.**
Receiver selection / activity / VFO/MR mode
**3.**
Indicator of the last reception / frequency offset of the last reception (x10 Hz)
**4.**
Channel parameters / the following symbols may be displayed:

**ATT 1, ATT 2** - attenuator enabled (quick on / change / off - `*` )
**DCS, CT** - type of the configured subtone – see section 2, item 4;
**HIGH, MID, LOW** – current TX power (quick change – long 6)
**R** - reverse mode enabled – (long 8);
**12,5k, 25k** - channel bandwidth – (quick change F+7)
**SCR** - analogue scrambler (2.3. Main menu, item 11)
**5.**
S-meter scale
**6.**
Receiver selection / activity / VFO/MR mode
**7.**
Reception – RX / Transmission - TX

**8.**
Battery charge indicator
**9.**
Memory channel name / frequency
**10.**
Assigned scan list (- first, - second)
 - the channel is in both scan lists
 - the channel is not in any scan list
**11.**
S-meter signal level
**12.**
Modulation type - AM/FM/SSB (switched with a long 7)

## 2. MENU.

### 2.1. Menu navigation.

**Use the** ▲ **/** ▼ **arrow keys, or type the item number directly on the keypad (01, or 22…)**
***Attention!!!*** *Menu items 2, 3, 4, 5, 6, 7, 8, 9, 10, 26 and 39 are set*
*individually for the A and B bands and for each frequency band (Band).*

### 2.2. Working frequency bands (Bands):

1.00000 – 108.99990 MHz; 109.00000 – 139.99990 MHz; 140.00000 – 199.99990 MHz
200.00000 – 279.99990 MHz; 280.00000 – 399.99990 MHz; 400.00000 – 669.99990 MHz
700.00000 – 3200.99990 MHz.
The precision of the frequency value depends on the step set in item 2 (Step).

### 2.3. Main menu.

**1.**
**Sql** – squelch sensitivity level, set simultaneously for the upper (**A**) and lower (**B**) bands (see also the description of item 35)
**2.**
**Step** – frequency step. (for CB = 5/10; Satcom, Avia = 5/25; everything else = 6.25/12.5).
**3.**
**Power** – transceiver TX power. **High / Middle / Low**.
***4.***
**R_DCS** – digital coded subtone for reception (Digital-Coded Squelch), *if the function is enabled, the squelch will open only after this subtone has been received. (applies to FM modulation only)*
***5.***
**R_CTCS** – analogue subtone for reception (Continuous Tone-Coded Squelch System), *if the function is enabled, the squelch will open only after this subtone has been received. (applies to FM modulation only)*
***6.***
**T_DCS** – digital coded subtone for transmission, *if the function is enabled, the transceiver will send this tone. (applies to FM modulation only)*
***7.***
**T_CTCS** – analogue subtone for transmission, *if the function is enabled, the transceiver will send this tone. (applies to FM modulation only)*
**8.**
**Shift** – sign of the transmit frequency shift (RX/TX split) **+**/**–**/**upc.**
*(upconverter - when a down-converter is used)*
**9.**
**Offs** – value of the transmit frequency shift.
**10. W/N** – the bandwidth used by the transceiver:
- **25 kHz** - Wide
- **12.5 kHz** - Narrow.
**11. Scrambl** – analogue scrambler
*transforms the original speech signal by changing its amplitude, frequency and timing parameters in various combinations (1-10 – masks the speech, 11-20 – changes the pitch of the speech).*

**12. BusyCL** – transmission is blocked on a busy channel: while the transceiver is receiving a signal, pressing PTT does not start transmission.
**13. Mem_ch** – save the frequency and the settings to a memory channel
*any change of the settings of the active channel (in channel (MR) mode) is stored only if it is confirmed through this menu item; if this is not done, the channel settings revert to the previously saved ones as soon as you switch to another channel or turn the radio OFF/ON.*
**14. Save** – battery saver (ratio between active time and sleep time). **MAX** – maximum power saving x10
*Maximum power saving is achieved with Save=Max together with DW=OFF. The optimum setting is 1:3. When it is on, the symbol* ***S*** *appears in the status line from time to time* ==*(see also the description of item 25 Roger (Roger=5)).*==
***15.*** **VOX** – voice-activated TX (1-10 microphone sensitivity)
*when you enter the menu with "M", VOX is blocked to prevent it from triggering on key presses.*
**16. Light** – screen backlight. It is configured in 2 stages: time and brightness:
 **BACKLIGHT TIME SETTING:**
**OFF** – full blackout (even the RX/TX LEDs stay dark);
**KEY** – the same as OFF, but the backlight comes on for 5 seconds when a front key is pressed**;**
**2, 5, 10, 20 sec**, **2 min** – backlight time. The backlight stays on for the selected time, but switches off only after reception has ended;
**ON** – backlight permanently on.
 **BACKLIGHT BRIGHTNESS SETTING:**
**bri 0-7 –** backlight brightness adjustment.
To set it, first set the backlight time, then enter the **Light** item again and set the brightness.
**17. DW** – dual watch mode for the frequencies on the A and B bands:
- **Chan_A / Chan_B** – enable the DW function.
- **SCAN** – the active band **A / B** stays the working one, the other one scans the channels of the active scan list.
- **OFF** – disable dual watch mode.
==**ATTENTION**: when background capture is switched on (long press of key 1), DW=ON is activated automatically *(the captured frequency is shown in VFO-B).*==
**18. Beep** – audible signals when the transceiver is switched on, when the battery is low, and when a frequency is detected in background frequency capture mode (key presses are not accompanied by a sound).
**19. TxTime** – limit on the duration of continuous transmission and of beacon operation.
**20. Scan** – the method of stopping or resuming scanning (this setting also applies to the spectrum analyser):

- **CO** – scanning resumes after the carrier disappears ==(optimum);==

- **TO** – resume scanning after a 5-second pause *(in the spectrum a strong signal may periodically drop out / stall, the "freeze effect");*
- **SE** – stop scanning completely once a signal is detected. The ▲**/**▼ keys resume scanning *(*==*when SE is selected*== *in the spectrum, frequencies that have already been picked up into the "Loot" are not "searched" again).*

**21. Name** – select the style used to display channel names (available options: **NAME** - name, **CHAN** - channel, **FREQ** - frequency, **NAME+F** - name + frequency).

**22. STE** – removes the hiss/noise/"pfft" at the end of a transmission. *(When PTT is released, a short 55 Hz tone is sent on the air, telling other transceivers that the transmission has ended and that they should mute the audio.)*

**23. Mic** – microphone sensitivity:

- **0** – thresholdless sensitive microphone (best with **tx_filt = 1-2)**;
- **1** – Minimum – (best with **tx_filt = 0-1)**;
- **2** – Medium (best with **tx_filt = 1)**;
- **3** – Boosted *(better for long-distance contacts; at short range an echo appears)* (best with **tx_filt = 1)**;
- **4** – Boosted **recommended** *(*for a quiet environment, best with **tx_filt = 1)**;
- **5** – MAX *(ambient background becomes audible)* (best with **tx_filt = 1)***.*

**24. SList** – select scan list **1** / **2** / **3** (3 - scans all channels from memory)

*Adding / removing the active channel to or from the scan lists (you can only add / remove in SList 1 and 2) is done with the F+1 combination from the main screen, which is confirmed by the icon from item 9 on p.2 appearing / disappearing.*

*While SList 3 is active, channels cannot be added or removed!*

*In addition, F+9 lets you assign 2 priority scan channels; for details see the section "KEY FUNCTIONS" (9 CALL).*

**25. Roger** – audible tone at the end of a transmission (2 working options to choose from)

*Additional Rogers 3-55 are test functions – do not scroll through them without a reason:*

*Roger 3 - frequency auto-capture with greater range (see the section "Key functions");*

*Roger 4 – Turns the auto-attenuator off (OFF);*

*Roger 5 - mode with improved power saving + speed-up of: dw switching, subtone measurement, sql checking in powersave. A different operating algorithm.*

*Roger 6 – Reverse TX frequency correction by AFC (to compensate for Doppler shift);*

*Roger 7 – Direct TX frequency correction by AFC*

*(Automatic TX frequency tuning by afc. After a signal is received, the radio remembers the frequency offset and corrects the transmission. The EXIT key resets the correction.)*

*Roger 8 – Software AGC from AM_fix in FM.*

**26. Modulat** – modulation mode **FM / AM / SSB** *(FM by default, works on receive only).*

**27. AM_fix** – enables AM AGC to improve reception of AM signals *(when this function is active, the registers are not adjusted in "frequency capture" mode in the spectrum if amplitude modulation is set).*

**28. AMf_lvl** – adjusts the AM AGC level *(under some conditions it reduces noise).*

**29. LNA_hi** – enables the low-noise amplifier *(in environments with strong interference it is better to switch it off).*

*When it is switched off the spectrum is "flat"; when it is switched on the spectrum "comes alive".*

*See the additional description of the MAN value in the description of the spectrum analyser mode registers.*

**30. rx_filt** – changes the tone of the received signal *(1 - boosts the lows, 2 and 3 - cut the lows and boost the highs (****3 is optimal****)*

**31. tx_filt** – changes the modulation on transmit (preset for the Tx3k register) *0 – stock, 1 – reduces it* ***(optimal)****, 2, 3 - increase the modulation; a squeal or squelch chopping may occur on the receiving transceiver.*

*If you run into problems, set menu items 30, 31 =* ***1****, restart the transceiver, then set them =* ***0****)*

**32. Del_ch** – delete a memory channel

**33. Reset** – reset the transceiver configuration:

==-== ==**VFO**== – reset the transceiver settings and the VFO bands

==-== ==**ALL**== ==– reset all transceiver settings, including== deleting the channels

==*(the calibrations are not affected by this).*==

**34. Re-name** – rename a channel (`*` - next character) – for newly saved channels, if no name is set, during scanning it is displayed as «**,,,,,,,,,»**; when entering a name, scroll past the empty characters with `*`

==**35. Preset**== ==– Select the working preset== ==**that is loaded by default**== ==(0, 1, 2)== ==for the operation of the radio.== ==**Calibrations and configuration are individual for each preset**====!==

==*(for each preset, on first load you must perform a full memory wipe (power on with PTT+EXIT held), then load the calibrations and the configuration (if needed) and set up all the items you require).*==

==Switching to the preset you need on the fly is done by powering the radio on with the corresponding key 0 / 1 / 2 held down.==

**36. Sql 2** – squelch sensitivity level for the **B** band.

*When you adjust* ***SQL*** *(menu item 1), the setting is applied to both the* ***A*** *and* ***B*** *bands at the same time.*

*When you adjust* ***SQL2****, a separate setting is applied to the* ***B*** *band. (The* ***B*** *band setting is reset whenever* ***SQL*** *in item 1 is changed.)*

**37. Loot** – the "Loot menu" automatically collects the frequencies on which reception occurred while scanning in the spectrum and in VFO (128 entries – on overflow the oldest ones are overwritten. Sorted from the most recently found; a duplicate filter is applied and detected subtones are displayed)

*If the frequency is already saved in memory, the channel name is displayed. (If the frequency is stored twice in the channel list, the name of the first channel in the list is displayed.)*

*The time elapsed since the last reception is also displayed.*

*When an entry is selected with the* ***M*** *key, the current frequency is transferred to the active VFO band.*

*Saving to memory from VFO is done via item 13. Mem_ch*

*The "Loot menu" is cleared after the transceiver is restarted.*

### 2.4. Hidden menu.

==***Without experience and the necessary instruments it is not recommended to change the parameters of items 41-53 of the hidden menu – changing these items affects the calibration of the radio.***==

==***Any adjustment of these items is done at your own risk !!!***==

==***It is strongly recommended to make a BACKUP of the radio's settings and calibrations before changing them!***==

The hidden menu appears if you power the radio on with **PTT** and the side function key **FN1** held down at the same time, and then release all keys *(release* ***PTT + FN1*** *after the splash screen goes out)*.

**38. F Lock** – select the frequency plan that permits transmission *(entering a frequency for reception purposes remains open across the whole 15.0 MHz – 1349.9999 MHz range):*

- **FCC** (144-148, 420-450);
- **CE** (144-146, 430-440);
- **GB** (144-148, 430-440);
- **LPD PMR** (433-435, 446-447) - this also locks all front keys except the ▲**/**▼ arrows (after the transceiver is restarted)

*For a band in* ***VFO*** *frequency mode, a frequency can be entered by scrolling with* ▲ */* ▼ *(within one VFO band).*

*For a band in* ***MR*** *channel mode, only pre-programmed channels can be selected by scrolling with* ▲ */* ▼ *;*

- **OFF** (136-240, 280-500) – the stock frequency range.

**39. Tx All** – select the transmit lock mode:

- **DEFAULT** – transmission in the bands selected in the previous menu item **36;**
- **DISABLE** – forbid transmission on all frequencies;
- **ENABLE** – allow transmission on all frequencies.

**40. Sat** – retunes the receive filters for the Satcom frequency band

- **OFF –** if the coils have been modified for Satcom reception;
- **ON –** if no modifications have been made.

==**41. F_Corr**== ==– correction of the reference oscillator frequency==

==**42. r.Open**== ==– manual adjustment of the SQL OPENING level by RSSI.==

==**43. r.Close**== ==– manual adjustment of the SQL CLOSING level by RSSI.==

==**44. n.Open**== ==– manual adjustment of the SQL OPENING level by noise.==

==**45. n.Close**== ==– manual adjustment of the SQL CLOSING level by noise.==

==**46. g.Open**== ==– manual adjustment of the SQL OPENING level by Glitch.==

==**47. g.Close**== ==– manual adjustment of the SQL CLOSING level by Glitch.==

==**48. a**== ==– service settings for the firmware's test functions====**.**==

==**49. b**== ==– service settings for the firmware's test functions.==

==**50. c**== ==– service settings for the firmware's test functions.==

==**51. d**== ==– service settings for the firmware's test functions.==

==**52. e**== ==– service settings for the firmware's test functions.==

**53. PWR** – TX power, stored in the calibrations *(on entry it shows* ***0****; scroll with* ▲*/*▼ *or press* ***EXIT*** *- the value will refresh).*

*To save a value, first select the frequency / band and the power level you want to trim (HIGH / MID / LOW). Then open the PWR menu item, change the value and press* ***M*** *to save.*

***The PWR value will be different for the beginning, the middle and the end of each frequency band, and for each power level!!!***

## 3. KEY FUNCTIONS.

**Short press** – press and release (standard).

**Long press** – at least 1 second (for most keys this is equivalent to the combination "**F + short press**").

**F + very long press** – 5 seconds (until the red LED blinks).

### ==3.1. Service combinations.==

==Functions available when the radio is powered on with keys held down:==

==-== ==**PTT+FN1**== ==– Enter the hidden settings menu (see section 2.4).==

==-== ==**PTT+EXIT**== ==– Full memory wipe (calibrations, configuration, all settings) –== ==**must be done with the cable DISCONNECTED**====; after power-on keep the keys held for at least 2 seconds.==

==-== ==**0**== ==– quick selection of preset 0 at the moment of power-on (see menu item 35).==

==-== ==**1**== ==– quick selection of preset 1 at the moment of power-on (see menu item 35).==

==-== ==**2**== ==– quick selection of preset 2 at the moment of power-on (see menu item 35).==

### 3.2. Front keys.

**M**

- short press **M** – enter the Menu
- short press **M** – leave the current Menu item, confirming the setting
- ==long press== ==**M**== ==– enter modem mode (TEST FUNCTION).==

▲/▼

- short press ▲/▼ – change channel / frequency by the set step
- F+ short press ▲/▼ – change channel / frequency in 1 MHz steps

**1 BAND**

- long press **1** – background frequency capture (an **x** appears on the screen)

==When background capture is switched on, DW is activated automatically.==

==*(When activity is detected, the captured frequency is copied into the*== ==***scratch memory***== ==*of VFO2 (temporarily). Any manipulation of VFO2 makes the captured frequency disappear. The captured frequency can be viewed in the Loot menu.)*==

*(If item* ***Roger=3*** *is set (****it is also recommended to set* *SQL=3, SAVE=1:3), the function runs as "long-range capture"; battery consumption increases and the radio may become sluggish.)*

- **F+** short press **1** – Add / remove the active channel to or from the scan lists *(you can only add / remove in scan lists 1 and 2* ***(****pressing F+1 adds/removes the current channel and automatically jumps up to the next nearest channel on which the same operation can be performed – if you are removing, it jumps to the next channel that can be removed from the current list; if you are adding, it jumps to the next one that can be added to the current scan list)*, which is confirmed by the icon from item 9 on p.2 appearing / disappearing.

While scan list 3 is active, channels cannot be added or removed!

- F+ very long press 1 – FM auto-beacon (the text **RXTX** appears) (the transceiver answers a call with a "beep") – during transmission the auto-beacon can be switched off by pressing any key. **W/N=12.5** is recommended.
- Pressing F+ very long 1 again – auto-beacon with background monitoring.

The run time depends on item 19. TxTime, where 1 min = 10 s of beacon operation / 2 min = 20 s of beacon / … / 9 min = 90 s of beacon / 10 min = 100 s of beacon. Optimal settings: txfilt=1, mic=4, ste=on. Leave beacon mode by pressing **EXIT.**

**2 A/B**

- long press 2 – switch between the upper (A) and lower (B) frequency
- F+ very long press 2 – FM auto-beacon (the text **RXTX** appears) (the transceiver answers a call with a "Predator chittering" sound) – during transmission the auto-beacon can be switched off by pressing any key.

Pressing F+ very long 2 again – auto-beacon that sets the DCS subtone according to the signal level. See the DCS-to-signal-level table below.

*Handy for testing and comparing different antennas. It shows not only the fact that the signal reached the beacon, but also the strength of the received signal.*

Leave beacon mode by pressing **EXIT.**

**Table of the F+2 / F+2 beacon DCS subtone against signal level**

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

The Quansheng UV-K5 and its variants are not laboratory measuring instruments. The signal level is read from the S-meter scale and may differ from values measured by other devices !!!

- unstable zone (AGC at work)

For stable testing it is recommended to set low TX power and to keep some distance between the radios.

**3 VFO/MR**
- long press 3 – switches between frequency (**VFO**) and channel (**MR**) mode
- F+ short press 3 – (in **MR** mode) switches to **VFO** mode, automatically copying the current frequency from **MR** into **VFO**. In **VFO** mode, F+ short press 3 -> switches to **MR** mode.
- F+ very long press 3 – AM auto-beacon (the text **RXTX** appears) (the transceiver answers a call with a signal in amplitude modulation) – during transmission the auto-beacon can be switched off by pressing any key. Leave beacon mode by pressing **EXIT.**

**4 FC**
- long press **4** – the Loot frequency list. Functions in the Loot menu:
***4*** *– adds/removes a frequency to/from the blacklist (Lock) until power-off.*
***0*** *(long) – clears the Loot blacklist and the ATT list.*
***M*** *– sends the current frequency to the active* ***VFO*** *band (when* ***MR*** *is active and a channel with that frequency exists, the radio switches to that channel). Saving to memory from VFO is done via item 13. Mem_ch.*
*When the transceiver is switched off, the Loot list is cleared.*
- F+ long press 4 – frequency capture; save it with the **M** key.
By default the UHF/VHF filters are disabled, as in the stock firmware, so only strong local signals or radios in the immediate vicinity are detected. To improve capture range and stability, select the filter you need by pressing 1 (VHF) or 2 (UHF).

*In capture mode the frequency and the subtone on the display "jump" (you see values being cycled through) until a capture happens. Once the captured frequency has been determined, the value stops.*

- F+ very long press 4 – enters PTT-Holder mode (holds the transmission until PTT is pressed again). Transmission is switched on directly by pressing

**PTT+FN1** at the same time.
Leave PTT-Holder mode by pressing **PTT** again.

**5 NOAA**
- long press 5 – switches on the spectrum analyser with hybrid squelch
- F+ short press 5 – starts the spectrum analyser tracking the frequency of the active **VFO / MR**

**6 H/M/L**
- long press 6 – switches TX power **HIGT / MID / LOW**

**7 VOX**
- long press 7 – changes the modulation **FM / AM / USB**
- F+ short press 7 – changes the channel bandwidth **12.5 / 25 kHz**
- F+ very long press 7 – AM tone generator. Keys:
**1, 2, 3** – duty cycle; **4, 5, 6** – delay; **7, 8, 9** – bandwidth (~25-1000k);
**0** – mixing in an FM tone; ▲**/**▼ – fine adjustment of the delay.

**8 R**
- long press 8 – switches on reverse mode: the receive and transmit frequencies are swapped (the symbol R appears next to the bandwidth)
- F + very long 8 – frequency and power randomizer (the symbol **r** appears) *(pressing PTT while F is active and the randomizer is on – transmits with the microphone switched off)*

**9 Call**
- long press 9 – dynamic volume (the symbol **D** appears)
(sometimes helps to smooth out the hiss/noise/pop at the end of a transmission)
- F+ short press 9 – adds the channel to the priority list used while scanning *(2 channels in ScList1 and 2 channels in ScList2, which are scanned every 3 steps of the scan list); pressing F+9 a third time switches the priority channels off. Nothing is shown on the display. If the same channel is added twice to the priority list, scanning may "stick".*

**0 FM**
- long press 0 – switches the FM radio on/off (you can leave it with EXIT)
*FM reception stops when a signal appears and resumes 5 seconds after the signal disappears. PTT also interrupts FM reception temporarily.*
***Controls in FM radio mode:***
▲*/*▼ *- change channel / frequency;* ***F+1*** *- switch VFO / MR;* ***F+3*** *– station search (once a broadcast is found the search pauses without saving automatically.* ▲*/*▼ *- continue the search);* ***M*** *- delete channel (in MR), save channel (in VFO);* ***F+6*** *– switch AGC (automatic gain control) on/off*
- F+ very long press 0 – automatically sets the subtone of the last reception (the symbol **A** appears)

**`*` SCAN**
- short press `*` – switches on the attenuator for the current frequency / channel (**ATT1** appears, on the next press – **ATT2**, then **ATT3**, and the fourth press switches it off);
- long press `*` – in frequency mode starts frequency scanning, in channel mode starts channel scanning *(according to the scan list selected in menu item 24.SList. If no channels have been added to the selected scan list, the radio may stop responding)*, (stop it with **EXIT**).
*If you need to skip a channel / frequency while scanning, you can switch ATT1, ATT2 or ATT3 on for it;*
- F+ short press `*` – scans CTCSS subtones on the current frequency.

==When the scan has finished, the== ==**M**== ==key can be used to set the subtone that was found as the transmit subtone for the active VFO band.==

**F #**
- short press F – enters option mode (the symbol **F** appears)
- long press F – switches the lock of the front keys on/off (**L** appears)
- While the **F** index is lit, and if the randomizer function is on (see section 3.1, item 8 R), pressing PTT transmits with the microphone switched off.

### 3.3. Side keys.

**IMPORTANT !!!** If, when configuring the radio through CHIRP or PSCPS, FN1 and/or FN2 are set to NONE (not assigned), the radio may become locked and ask for a code at power-on.

![screenshot](images/p16_1.png)

**Side "push-to-talk" key [PTT]**

- pressing it starts transmitting on the air
- pressing it together with any front key sends a **DTMF** code

**Side function key [FN1]**
**(default values)**

- short press – opens/closes the squelch
- long press – switches the flashlight on/off

**Side function key [FN2]**
**(default values)**

- short press – switches TX power **HIGT / MID / LOW**
- long press – starts the broadcasting beacon on the selected frequency *(works when menu item 17 -* ***DW*** *is off; stop it with* ***EXIT****)*
- pressing it while PTT is held sends a **1750 Hz** tone

If the firmware is installed over stock firmware, or together with your own configuration file, the default assignments of the [FN1] and [FN2] keys may be different, because these assignments are stored in the configuration file.

**User functions of the [FN1] and [FN2] keys**

The FN1 and FN2 functions can only be changed through software (CHIRP, for example) and cannot be set or reassigned from the radio's menu.

**The following choices are available:**

**NONE** – nothing selected,

**FLASH LIGHT** – flashlight,
**POWER** – switch TX power, **MONITOR** – open the squelch,
**SCAN** – scanning,

**VOX** – voice-activated TX,
**FM RADIO** – FM radio,

**1750 Hz** – send a 1750 Hz tone

### 3.4. Entering a frequency on the main screen.

To enter a frequency manually on the main screen you first have to switch to frequency mode (you switch between frequency and channel mode with a long press of the **3 VFO/MR** key). **VFO** then appears on the left-hand side of the screen, opposite the frequency.
Next, enter the frequency.
To enter the decimal point, use the key

**Examples:** 140 *→* = 140.00000 or 433*875 *→* = 433.87500

Frequency entry can be cancelled with the key

### 3.5. Scanning in VFO and MR modes.

**Scanning within set frequency limits in VFO mode**

- switch VFO1 and VFO2 to frequency mode
- set the start (VFO1) and end (VFO2) limits of the scan
- make the upper VFO1 the active one
- start the scan with a long press of the **`*` Scan** key
- it runs in a loop within the limits (from VFO1 to VFO2)
- the ▲**/**▼ keys change the scanning direction
- the scan is stopped with **EXIT**
(the frequency then returns to its initial value – VFO1)

*Note 1: If you start the scan while VFO2 is active, the scan runs outside the set limits, and when it is stopped the frequency does not return to its initial value.*

*Note 2: The scan step = the step set for band A (item 2 of the settings menu).*

**Scanning in channel (MR) mode**

- switch to channel mode
- if necessary, select SList1, SList2 or SList3 in menu item 24
- start the scan with a long press of the **`*` Scan** key
- it runs in a loop according to the selected SList
- the ▲**/**▼ keys change the scanning direction
- if the scan sticks on one of the channels (because of interference), you can switch the attenuator on for that channel (**ATT1** or **ATT2**) by pressing **`*`**
- the scan is stopped with **EXIT**

- ==The **CHANNEL = PRESET** function:==
- ==set the end frequency in offset, set shift – scn (the scanning direction), add the channel to the scan list you need.==
- ==After a scan is started in channel mode, an additional scan is performed within the limits of this setting when this channel is reached.==

## 4. SPECTRUM ANALYZER

### 4.1. Main spectrum mode (hybrid squelch) — how to enter:

- long press **5** – switches the spectrum analyzer on with hybrid squelch
- **F** + short press **5** – starts the spectrum with frequency tracking in VFO
- **IMPORTANT!** *If the spectrum analyzer is started from a channel or from VFO with the RX/TX offset enabled (items 8 and 9 of the settings menu), this offset will also be applied when transmitting from the active frequency capture mode.*

![screenshot](images/p19_1.png)

![screenshot](images/p19_2.png)

**The spectrum analyzer uses a hybrid squelch:**

when the squelch threshold is lowered, it opens only on signals that look more like channel signals, with a normal bandwidth and frequency.

1. Preset (frequency plan) – **3 / 9**
2. Number of scan steps – **2 / 8**
3. Scan step size – **1 / 7**
4. Current, or last detected, receive frequency (the one on which a signal was found) – the frequency changes when a signal is detected with a level above the squelch threshold (10).

5. Channel name (shown provided that the frequency is already stored in channel (MR) mode memory. If the frequency is stored twice in the channel list, the name of the first channel in the list is shown. If the channel is saved but no name has been given to it, «**,,,,,,,,,**» is displayed — see the description of item **34 Rename** of the settings menu for how to give a channel a name)
6. Subtone of the received signal (shown if present)
7. Receiver bandwidth – **6**
8. Modulation type AM/FM/USB – **0**
9. Battery charge indicator
10. Squelch (SQ) level – `*` / **F**
11. Start frequency of the scan range – you can shift the whole range with ▲/▼, or enter the start frequency from the keypad: press **5**, then in "free entry" mode enter the new start frequency immediately after ----- appears; in preset mode use **F** to select **f start** and enter MHz, the `*` separator, kHz and Hz, then press **M** to apply.
12. Spectrum frequency step – **4** (used to shift the whole scanned range with ▲/▼ by the set step)
13. End frequency of the scan range – you can shift the whole range with ▲/▼, or enter the end frequency from the keypad: press **5**, use **F** to select **f end**, enter MHz, the `*` separator, kHz and Hz, then press **M** to apply *(in "free entry" mode the end frequency is corrected according to the number and size of the steps, in multiples of 16/32/64/128; in preset editing mode the exact frequency is set).*

**long press 4** – enter Loot. Functions in the Loot menu:

***4*** *– adds the frequency to the blacklist (Lock) until power-off.*

***0*** *– clears the spectrum Loot blacklist.*

*The Loot list is cleared when the transceiver is switched off.*

### 4.2. Additional function keys in spectrum analyzer mode:

**FN1** – adds the current frequency to the scan blacklist (128 frequencies – on overflow the earliest ones are overwritten) – press until the red LED blinks for the first time (after the second blink of the LED the blacklist is cleared).

- The blacklist is reset after the radio is switched OFF/ON.
- If you need to keep some frequencies with constant interference permanently, you can put them into the stored blacklist. To do this go to the Presets menu (enter with **M**, scroll with **M** and select **SAVE**), then press up ▲ (this stores the last 16 frequencies of the blacklist).
- The stored blacklist is cleared by a **long press of FN1** – until the red LED blinks for the second time (in the spectrum), followed by saving in the Presets menu.

***!!! For the stored blacklist to work correctly***, *it is recommended to clear the blacklist with a long press of FN1 and save it the first time you start the scanner after installing the firmware.*

**FN2** – frequency skip – press while a signal is being received (the frequency is skipped only on the current scan pass; on the next pass it takes part in scanning again)

– switches the display backlight off / on in spectrum mode (press when nothing is being received).

### 4.3. Spectrum analyzer settings.

You can work in the spectrum analyzer either in "free entry" (range) mode or with predefined presets. The "free entry" settings are not saved and are cleared when the radio is switched off/on. Changes to the presets can be saved if required.

By default the following presets are preconfigured for scanning in spectrum analyzer mode:

| Preset | Range, MHz | Step | Modulation | Bandwidth |
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

**IMPORTANT:**
The presets can be edited to suit your needs, but note:

- Preset names cannot be edited.
- Changes to the bandwidth and the modulation are not saved.

### 4.3.1. Working in "free entry" mode

Free entry is not tied to a particular band and its settings are not saved.

To set the start frequency of the scan range press **5** – the scan start frequency entry window opens (---------). Enter the number of MHz, the decimal point with `*`, then the kHz and Hz figures. Press **M** to confirm the value entered.

In "free entry" mode the end frequency is set automatically from the step – 1 / 7 – and the number of steps – 2 / 8 (*if you try to change the end scan frequency via* ***f end***, *the end frequency is adjusted to the number of steps in multiples of 16/32/64/128*).

When the start scan frequency is changed, the whole range together with all its settings — number of steps, step size, modulation and so on — moves to the new start frequency. *(for example: you were scanning the 400–401.6 MHz range (1.6 MHz wide) / 128×1 steps with a 12.5 kHz bandwidth. If you enter: 5 -> ------- -> 510 -> M, the whole range shifts from 400–401.6 to 510–511.6 and all the other settings are kept)*

To change the modulation, the step, the bandwidth and so on – see section 4.1.

To set exact values for the scan range you have to use the settings of preset mode.

### 4.3.2. Editing presets:

To edit the frequency range of a preset press **5** – the scan start frequency entry window opens (---------). Use **F** to select the parameter to be changed: the start (**f start**) and / or the end (**f end**) frequency of the preset. Enter the number of MHz, the decimal point with `*`, the number of Hz, then press **M** (the values are reset when the transceiver is restarted unless you save them through the additional menu).

- Besides the frequency, the preset settings also let you change the number of scan steps and the step size.
- If you need to change the step as well as the frequency, change the start frequency FIRST, then the step, then the end frequency, after which you can do **SAVE**.

**ATTENTION:** when editing presets it is important to keep their original order *(it is not advisable to change the 144–148 MHz range to 27–50 MHz)*, and also to avoid overlapping ranges *(presets set to 144–149 / 146–200 / 188–205 will cause a conflict).*

### 4.3.3. Setting the additional spectrum analyzer parameters:

Press **M** – the first parameter of the additional menu appears at the top (**Mult: OFF**); each further press of **M** scrolls through the parameters in a loop. Stop at the parameter you need and select the required value (state) of that parameter with ▲ (accept or on) / ▼ (cancel or off).

**Short description of the additional spectrum analyzer parameters:**

**Mult** – multi-preset, scanning all the selected presets one after another (keys **3/9** – select a preset; key **4** – add a preset to / exclude it from scanning (added presets are marked with the suffix fc); long press **4** – exclude all presets from the multi-scan; up key ▲ – start; to leave multi-preset mode press **M** + down ▼, or **EXIT**)

**ATT** – attenuator

**Turbo** – turbo scanning mode (on – ▲ / off – ▼) – scanning in accelerated mode: accuracy and sensitivity are lower but the speed is higher, so weak signals may be missed. Can be stored with save:on

**SQ** – interference filtering level for the hybrid part of the spectrum

**Delay** – signal exposure time (higher values increase the sensitivity but slow the scan down, and the other way round)

**Lna** – switches on the low-noise amplifier (unlike **LNA_hi** from item 29 of the main menu it has a higher gain value – about 10% stronger)

**EXP** – "spectrum exposure" mode (you can move the cursor with the `*` and **F** keys instead of the squelch threshold bar, to read the frequency of the peaks)

**SAVE** – saves the settings, including the presets, to permanent memory (up ▲ – write, down ▼ – back)

**ECO** – economy mode that works by slowing the scan down

### 4.4. Active frequency capture mode — "detailed view".

**VFO-PRO (entered from the main spectrum mode by pressing PTT)**

![screenshot](images/p24_1.png)

In frequency capture mode, pressing PTT to transmit applies the offset and the subtone, provided that this frequency was saved in memory with these settings.

![screenshot](images/p24_2.png)

![screenshot](images/p24_3.png)

1. S-meter scale
2. Channels found from the "Loot menu" can be scrolled – **1 / 7;** added to the blacklist – **4**
3. Squelch level – `*` / **F**
4. Current receive frequency (tuning – ▲**/**▼)
5. Subtone found for the current frequency (if present)
6. Register setting mode – **M / EXIT**

### 4.5. Registers of the active frequency capture mode.

While AM FIX is switched off, the manual LNA and PGA settings are not reset until the transceiver is restarted.

The DEV and Tx3k parameters are written to the calibration data when you leave the spectrum analyser.

**xtal** – fine adjustment of the receive bandwidth (for non-standard signals). (stock = 2)

**LNAs** – coarse adjustment of the LNA low-noise amplifier (stock = 3)

**LNA** – fine adjustment of the LNA low-noise amplifier

When you change the **LNA** and **LNAs** items in the registers of the active frequency capture mode and then save them, menu item 29 **LNA_hi** switches to manual control (**MAN**).
To return to automatic control, open the settings menu, press **M** twice on item 29 **LNA_hi** (**LNA_hi** switches to **ON**), and then save the settings in the presets menu by selecting **SAVE: ON –** ▲.

**DEV** – transmit channel width (stock = 1280)
(a value between 1200 and 1450 is recommended, default = 1400)

**SCR** - manual adjustment of the scrambler inversion frequency when the scrambler is on.
(default = 5150)

**Tx3k** – transmit modulation adjustment (default = 65531)
(kept in memory until menu item 33 - **tx_filt** is applied)
Tx3k has the following proven values:

- 62731 – stock
- 44831 – optimum
- 37431 – overdriven (for SATCOM and PMR)

**03t** – fine adjustment of the audio filter width (300 Hz), for TX
(default = 36873; optimum = 36600)

**AFC** - switches on automatic receive frequency control

**AFCR (AFC range)** – sets the AFC range (stable at 1-5 / optimum = 6)

**c0db** – microphone adjustment

**P (Peak (rssi))** – an alternative signal strength indicator for strong signals
(works best at frequencies above 1 GHz)

### 4.6. Key assignments in the spectrum analyser modes

| **Key** | **Mode** | **Function** |
| --- | --- | --- |
| **M** | Main mode | Selects the additional parameter to be adjusted |
| | Frequency capture | Selects the register to be edited |
| ▲<br>▼ | Main mode | Tunes the spectrum frequency |
| | Additional parameter setup | Changes the parameter value |
| | Frequency capture | Tunes the frequency |
| | Register editing | Changes the register value |
| **EXIT** | All modes | Cancel / Back |
| **PTT** | Main mode | Enters frequency capture mode |
| | Frequency capture | Starts transmitting, "TX" |
| **FN1** | Main mode | Adds the current frequency to the blacklist<br>(*the RX/TX LED blinks red to confirm the selection*)<br>*No transmission takes place, this is only an indication!!!* |
| | Frequency capture | Switches the squelch off / on |
| **FN2** | Main mode | Switches the backlight off / on (when nothing is being received)<br>Skips the frequency on the current scan pass (while a signal is being received) |
| | Frequency capture | Switches the backlight off / on |

## 5. FREQUENTLY ASKED QUESTIONS, POSSIBLE PROBLEMS, AND HOW TO SOLVE THEM.

| **No.** | **Problems**<br>**Questions** | **How to solve them**<br>**Comments, answers to questions.** |
| --- | --- | --- |
| ==1== | ==There is snow on the screen when the radio is switched on.== | ==You must clean the radio (see section 3.1. Service key combinations) and then load the calibration data (first your own factory calibration, then the calibration supplied with the firmware).== |
| ==2== | ==When you try to change the frequency in VFO mode, the frequency is not set== | ==1. Check whether the step set in item 2.Step matches the frequency you need.==<br>==2. The cleaning procedure after installing the firmware was probably not completed correctly (the service cable was not disconnected while cleaning). – run the cleaning again / load the calibration data / carry out the setup.== |
| 3 | On which frequencies may I transmit? | There are civil radio communication frequencies that are allowed for free use. As a rule these are:<br>CB (25.165 – 29.445 MHz) with a TX power of 4.0-12.0 W<br>LPD (433.075 – 434.775 MHz) with a TX power of 0.01 W<br>PMR (446.00625 – 446.19375) with a TX power of 0.5 W<br>In some countries the FRS and GMRS bands are also used. |
| 4 | On which frequencies may I not transmit? | Without special permits, transmitting outside the civil bands is prohibited by law. All the other frequency bands are used by other services, from radio amateurs to government services, including satellites, cellular networks, air traffic controllers and aircraft, weather stations, river and maritime communications, the military and others. If you cause interference to the operation of any of these services, you may be held liable under the law in force in your country. |
| 5 | On which frequencies do the Quansheng UV-K5 receiver and transmitter work | In the Karina firmware, reception and transmission are open on all bands (see section 2.2. Operating frequency bands (Bands)).<br>On radios without hardware modifications you may transmit without the risk of burning the radio only in the operating bands declared by the manufacturer: 136-174 MHz / 400-470 MHz |
| 6 | What happens if I transmit without an antenna? | Transmitting without an antenna, or with an antenna tuned for a different frequency band, burns out the radio's output stage. |
| 7 | Does the radio transmit on the CB band? Can I talk to | In the Karina firmware the 27 MHz frequency band is open for reception and transmission by default.<br>To receive, you must fit an antenna tuned to this frequency band.<br>However, transmitting in this frequency |

| **No.** | **Problems**<br>**Questions** | **How to solve them**<br>**Comments, answers to questions.** |
| --- | --- | --- |
| | truckers? | band from radios without hardware modification does not give usable communication (because the TX power is far too low); at the same time, because of the physical characteristics of the radio, trying to transmit in this band creates interference on the air band and also burns out the radio's output stage. |
| 8 | Why can't anyone hear me on CB? | In its factory state the radio's TX power in the CB band does not exceed 0.01 W. Therefore, without physical modifications, transmitting in this frequency band is not only useless but also dangerous for the radio itself. |
| 9 | Why is communication poor in a car? | The car body shields radio signals. For stable communication it is recommended to fit an external antenna outside the car body. |
| 10 | Why flash the radio at all | A stock radio "out of the box" works reliably and performs its functions. Modified firmware extends the functionality of the radio, offering additional and more flexible (professional) settings, faster scanning, scanning with a graphical display (spectrum analyser mode), and so on. |
| 11 | Which firmware is the best? | The one that best suits your needs |
| 12 | How do I back up the factory firmware? | There is no point in saving the factory firmware, because it is freely available on the internet and on the manufacturer's website. It is far more important to save the original calibration data (which may be unique to your radio) and the configuration file. This is done with the k5prog program. |
| 13 | The computer does not see the radio connected through the built-in Type-C port | The Type-C port built into the radio is intended for charging the battery only.<br>Flashing is done with a special programming cable with a KENWOOD type connector. (a cable from analogue Baofeng radios and similar will do) |
| 14 | Will a cable from a Baofeng work for flashing and configuring? | Yes, it will (one from analogue radios) |
| 15 | How do I start flashing | Any flashing should start with a check of the battery charge. If the battery is charged below 50% (~7.2 V), the flashing process may be erratic or incomplete.<br>For flashing you should buy or make a programming cable with a KENWOOD type connector, and install the driver for this cable on your PC. Prepare the flashing program. Prepare the firmware itself. Connect the switched-on radio to the PC with the cable you obtained and use the program to back up your own calibration data and the configuration file. Connect |

the radio in flashing mode. Use the program to run the firmware file.

**16. Where can I get detailed flashing instructions?**

See the section QUICK GUIDE TO FLASHING THE QUANSHENG UV-K5 AND ITS MODIFICATIONS.

**17. The computer does not see the radio**

- The cable is not pushed all the way into the radio (the first time it is inserted the cable goes in very tightly, often until it clicks).
- The cable drivers are not installed, or the wrong drivers are installed.

**18. Which program should I flash with?**

Modified firmware should be flashed as follows:
- the UV-K5, K5(8) and K5+ versions should be flashed with k5prog-win — version 1.26 is recommended
- the UV-K5+ versions (with a Type-C port) should be flashed with k5tools

**19. I flashed the radio, but on power-up it asks for some password.**

Try all digits 000000, or 111111, or 123400, or hold MENU+EXIT on the switched-off radio and, while still holding them, switch it on.

Also, if during configuration through CHIRP or PSCPS the side keys FN1 and/or FN2 are set to NONE (not assigned), the radio may lock up and ask for a code at power-up.

If that does not help, clear the radio's memory using the REBORN firmware — see section 6 of this manual.

**20. Which program should I use to program (configure) the radio?**

CHIRP or PSCPS.

To use CHIRP you have to load the module.

**21. What is CHIRP and what can it do?**

It is a program for programming radios. It edits channels and turns various functions on and off, including those that are not available from the radio's own menu.

**22. I loaded my saved frequencies (from another firmware) or somebody else's frequency file, and the radio behaves incorrectly**

Configuration files from different firmware versions can make the radio work incorrectly, so loading them is not recommended. Loading other people's configuration and settings files is not recommended either.

If you need to write frequencies from somebody else's file (or from your own file but made with another firmware), use CHIRP: open the other file, read your radio — a second tab will appear; copy the frequencies you need from the other file's tab and paste them into the tab of your radio's file. Before reading files, do not forget to load the corresponding module.

**23. Does the radio have encryption?**

The radio has no signal encryption, but it does have a scrambler (voice masking) function. Please note that under the legislation

of many countries the use of encryption, scramblers and other signal-masking functions in civil radio communication is prohibited by law.

**24. Why does the green LED light up on reception while the speaker stays silent?**

- check whether you have receive subtones set (R-DCS and R-CTCS);
- check that both radios use the same modulation (FM in particular).

**25. What is a subtone?**

A subtone is an additional signal, inaudible to the human ear, that is transmitted together with the voice. It works as a kind of "friend or foe" identifier (by filtering the incoming signal). When a subtone is configured, your radio rejects every signal on that frequency and opens for reception only when it detects a signal carrying the same subtone.

A radio without a subtone, on the other hand, will hear all other radios on reception, both those that use a subtone and those that do not.

**26. What is the non-standard 55 Hz subtone that the scanner detects?**

See the description in the Karina firmware manual, item 22, p. 5.

**27. Why do I hear one correspondent but not the other?**

It means that the signal from one operator is strong enough for you to hear him, while the signal from the second one is too weak.

This may be caused by your antenna not being very efficient, or by one of the operators being closer to you, or by the second operator's signal simply being too weak.

The opposite is also possible: the signal from one of the correspondents is so strong that it overloads your receiver, which then "chokes" on the excessively strong signal and goes silent.

**28. Why do I set the radio to scan frequencies and hear nobody?**

To hear somebody you first have to decide where to scan. Scanning "everything at once" will not get you anywhere.

For example: you want to scan the 100–200 MHz band with a 25 kHz step (the scan speed in frequency mode is about 15 frequencies per second), which gives 100/((0.025)*15) = 266 seconds (almost 5 minutes) for one scan cycle. It is far more effective to narrow the search range, or to start scanning in spectrum analyser mode using the configured presets.

**29. Can the radio be used to call for help?**

In exceptional cases, and only **when there is a direct threat to the life and health of people and there is no way to call for help by other technical means of communication**, you may send an SOS or MAYDAY distress signal.

**30. Which frequencies are best for calling for help so that I am heard?**

There are no universally accepted distress frequencies. There are maritime, river,

mountain-emergency frequencies and so on. These frequencies may also differ depending on the region and the country. When planning a trip to a particular region, it is recommended at least to find out which emergency communication frequencies are in use there.

There are, however, generally accepted calling frequencies on which you have a better chance of being heard:

433.500 — the general calling frequency of the 70 cm band
446.09375 — the general calling frequency of the PMR band
145.500 — the general calling frequency for radio amateurs (for communication between radio amateurs who hold licences and permits)

Depending on the region, these frequencies may differ as well.

It is not recommended to occupy these frequencies for long conversations. You can always make contact on them and then move to other frequencies by agreement.

**31. What is the S symbol that lights up from time to time in the top left corner?**

See the description in the Karina firmware manual, item 14, p. 5.

**32. Why, when I change the TX power (or the bandwidth, or the modulation, or the subtone, or the frequency offset), are the changes not saved after I switch to another channel and back, or switch the radio off and on?**

See the description in the Karina firmware manual, item 13, p. 5.

**33. When I press PTT it shows DISABLE — what should I do?**

See the description in the Karina firmware manual, items 36 and 37, p. 7.

**34. I connected a Type-C cable to the radio, but it is not charging**

Charging over Type-C is an additional option. It starts at a lower battery voltage and does not charge the battery up to its nominal level. Whenever charging through the cradle is possible, use the cradle.

**35. My battery voltage is displayed incorrectly — what should I do?**

If the battery voltage shown on the radio's display is implausibly low (~0.25 V) or implausibly high (600 V), this is the first sign that your calibrations are corrupted: you have to load the stock calibrations first and only then the Karina ones. If that does not help, clear the memory as described in the firmware manual and then install the firmware and the calibrations again.

If the voltage is displayed more or less correctly, with a deviation of about 0.2–0.5 V from the value measured with a multimeter, this is the normal situation with the factory calibrations. It can be adjusted with a HEX editor by changing the value of cell 140/6 of the calibration file (for me this value is =B0, but yours may differ).

**36. Why does it show 6.0 V while the radio is already switching off?**

The battery's operating voltage range is ~6.0 V – 8.4 V

~8.4 V = 100%
~7.2 V = 50%
~6.0 V = 0%

Discharging the battery below 4 V leads to its degradation.
