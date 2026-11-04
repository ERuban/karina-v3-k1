## FLASHING the Quansheng UV-K5V3 and K1 radios

### and working with CHIRP

**BEFORE YOU DO ANYTHING AT ALL:**

**1.**
**Make sure you have a K1 or a K5V3 version!!!**

**Version V1 carries no marking.**
**Versions V2 and V3 usually carry the corresponding marking on the label**
**under the battery.**

![screenshot](images/p01_3.png)

![screenshot](images/p01_1.png)

**Firmware is NOT interchangeable between versions. If you try to flash a radio**
**with firmware meant for another version, you end up with a bricked radio.**

V1 versions have a bootloader starting with 2, 3, 4 or 5
V2 versions have a bootloader starting with 1
V3 versions have a bootloader starting with 7

You can check this in k5prog-win with the radio connected in flash mode:

![screenshot](images/p01_2.png)

**Make a BACKUP of the stock calibrations**

**CONTENTS:**

**1. A BRIEF OVERVIEW OF INSTALLING THE KARINA (Autumn rain) FIRMWARE**
**on the Quansheng UV-K5(V3) and UV-K1 radios.**

**2. The detailed firmware installation procedure.**

**3. USING CHIRP.**
3.1. Downloading the module
3.2. Using the module with CHIRP (Karina)
3.3. Copying frequencies from someone else's file.

**4. FREQUENTLY ASKED QUESTIONS, POSSIBLE PROBLEMS AND HOW TO SOLVE THEM.**

## 1. A BRIEF OVERVIEW OF INSTALLING THE KARINA (Autumn rain) FIRMWARE

**on the Quansheng UV-K5(V3) and UV-K1 radios:**

**These instructions are for flashing the K5(V3) or the K1 only.**
**Trying to load K5V3 (or K1) firmware into a K5V1 radio = a bricked radio.**

**If you already have flashing experience, this short procedure is for you.**
**If you do not, a more detailed procedure with explanations and pictures follows below.**

**Before flashing, CHARGE THE BATTERY COMPLETELY.**

**A BRIEF OVERVIEW OF THE BACKUP AND THE FLASHING**

**1.** Switch the radio on and connect it over USB Type-C (or with a Kenwood cable).

**2.** Make a backup of the factory calibrations and of the configuration.

**3.** Switch the radio off, then switch it on while holding the PTT key.

**4.** Install the firmware with whichever flashing tool you prefer
(the file with the `packed` index – for the factory flashing tool **qpscps** / the file WITHOUT the
`packed` index – for any other flashing tool).

**5.** **DISCONNECT THE CABLE FROM THE COMPUTER!!!** Switch the radio off, then switch it on while
holding **PTT+EXIT** (hold for about 2 seconds) – the memory is erased.

**6.** Open the flashing tool again and write the factory calibrations back.

**7.** Write the calibrations that are supplied with the **Karina** firmware.

**8.** Write the configuration back (if required).
Alternatively, set everything up by hand through the radio's menu or through CHIRP
*(only configurations from previous versions will work; configuration files from other*
*firmware*
*will not).*

**ATTENTION!!!**
**If you configure the 3 presets separately (see item 35 of the settings menu), you must**
**carry out steps 5-8 separately for each of them, selecting the required preset in item 35**
**beforehand. !!!**

**A reminder:**

**Calibrations and the configuration are read and written** with the radio switched on
in normal mode.

**Flashing** is done with the radio switched on in flash mode (with the radio off, hold PTT and,
without releasing it, switch the radio on). The screen will stay dark, and the flashlight LED
will light up to indicate that the radio is in flash mode.

## 2. THE DETAILED FIRMWARE INSTALLATION PROCEDURE

**Before flashing, CHARGE THE BATTERY COMPLETELY.**

**1.** Switch the radio on and connect it over USB Type-C (or with a Kenwood cable).

**!!! Quansheng UV-K1 radios made for the Chinese market** have problems with the
USB Type-C connection; it is better to use a Kenwood cable with them.

![screenshot](images/p03_1.png)

Version for the European market

Version
for the
Chinese
market

**2.** **MAKE A BACKUP OF THE CALIBRATIONS AND OF THE CONFIGURATION**

To do this, open **k5prog-win** (version v0.1.26 is recommended) and make the
backup:

Calibrations: press **read calibration** and save the factory calibrations.
Configuration: press **read configuration** and save the factory configuration.

![screenshot](images/p03_2.png)

**3.** Switch the radio off, then switch it on while holding the PTT key.

**4.** Open the native program **qpscps** ( https://en.qsfj.com/support/downloads/8740 ),
select the COM port and the flashing menu (alt+D, the third item).

![screenshot](images/p04_1.png)

Give the path to the **packed** file and flash the radio by pressing **Update**.

![screenshot](images/p04_2.png)

*(If you are flashing online through the site https://armel.github.io/uvtools2/, then on the* ***Flash***
***Firmware*** *tab press* ***Choose file*** *and select the firmware without the* ***packed*** *index,*

![screenshot](images/p04_4.png)

![screenshot](images/p04_3.png)

*press* ***Flash firmware****, select the* ***COM port*** *and flash the radio.)*

**5.** **DISCONNECT THE CABLE FROM THE COMPUTER!!!** Switch the radio off, then switch it on while
holding **PTT+EXIT** for about 2 seconds – the memory is erased.

**6.** Open **k5prog-win** again and write the factory calibrations back with the
**Write calibration** button.

![screenshot](images/p05_1.png)

*(This can also be done through the site https://armel.github.io/uvtools2/ (if you saved the calibrations*
*with* ***k5prog-win****, you must change the file extension from* ***bin*** *to* ***dat****). To do this, on the*
***Restore Calib*** *tab select the required file with the* ***Choose file*** *button, press* ***Restore***
***Calibration Data****, select the* ***COM port*** *and write the calibrations.)*

![screenshot](images/p05_3.png)

![screenshot](images/p05_2.png)

**7.** Write the calibrations once more, this time selecting the Karina calibrations (at the time of
writing these instructions this is **calib5**) – following the same procedure as in step 6.

**8.** Write the configuration back using **k5prog-win** and the **Write configuration** button.
*(Only configurations from previous versions will work; configuration files from other firmware*
*will not.)*

![screenshot](images/p05_4.png)

## IF YOU NEED TO MOVE AWAY FROM THE KARINA FIRMWARE

(because its memory layout differs from that of other firmware)
you must do the following:

**1. Erase the memory** (switch the radio off, then switch it on while holding the PTT+EXIT keys (hold for about 2 seconds))

**2. Install any other MOD FIRMWARE** (the stock firmware will not do, because it does not allow calibration data to be written)

**3. Write back your original stock calibration data.**

**4. Use the radio**, or install anything else you like (including the stock firmware), as you prefer.

## 3. USING CHIRP

### 3.1. Loading the module

**IMPORTANT!!!** At the moment there is no dedicated CHIRP module for the Karina firmware. There are modules written for other firmware that are more or less compatible with Karina. The module listed below was originally written for the F4 firmware and has been adapted to Karina in some places. Even so, you should not change everything in sight through CHIRP, because compatibility is not complete.

When using CHIRP you have to load a module into it (*for Karina use the module from the archive*; **for other firmware you must choose the module that matches it**). To do this, start CHIRP, click "HELP" and enable developer mode. Then restart CHIRP, open the "File" menu, select "Load module" and choose the file from the archive.

![screenshot](images/p07_1.png)

![screenshot](images/p07_2.png)

**!!! IMPORTANT:** the module is unloaded when CHIRP is closed, so it has to be loaded again every time you start CHIRP.

**Next:** Radio -> Download from radio -> select the COM port -> Vendor (Quansheng) -> in the Model field, the module for your firmware.

![screenshot](images/p07_4.png)

![screenshot](images/p07_3.png)

### 3.2. Using the module with CHIRP (Karina)

As stated above, it is not advisable to change every function in CHIRP, because the module is not fully compatible. Below is an example of what can safely be edited (**marked in green**) and what you are strongly advised not to touch (**marked in red**):

**On the first tab**, with the memory channels, everything can be edited safely.

**On the second tab, Basic Settings**, you can freely change the following functions (all of them except the greeting message can also be changed from the radio's menu):

![screenshot](images/p08_1.png)

**On the second tab, Programmable Keys**, you can change the settings of the FN1 and FN2 side keys. These settings can only be changed from the software; they cannot be changed from the radio's menu:

![screenshot](images/p08_2.png)

Make sure that values are assigned to the side keys for both a short press and a long press (if NONE is set, the radio locks up and asks for a code!).

**On the second tab, ScanList**, you can set the default scan list and choose the priority channels for scanning in scan lists 1 and 2 (these settings are available both from CHIRP and from the radio's menu):

![screenshot](images/p09_1.png)

**On the second tab, Unlock Settings**, you can select the transmit lock for the frequency plan (these settings are available both from CHIRP and from the radio's hidden menu):

![screenshot](images/p09_2.png)

**On the second tab, FM Broadcast Receiver**, you can assign the FM broadcast station frequencies stored in memory (these settings are available both from CHIRP and from the radio's hidden menu):

![screenshot](images/p09_3.png)

### 3.3. Copying frequencies from someone else's file

It is not advisable to load someone else's frequency file, or a file from different firmware, into your radio. CHIRP and PSCPS essentially load a Configuration (the radio's settings), and its structure may differ between firmware versions (and even between different releases of the same developer's firmware).

Loading such a foreign configuration file may make the radio unstable (no reception, poor reception, problems with transmission or modulation, and so on).

**If you need to copy frequencies from someone else's file into a radio running Karina, do the**
**following:**

- Open it in CHIRP (loading the required module first, if necessary — the modules may differ from one firmware to another)
- load the module for Karina
- connect the radio to the computer and choose Radio -> Download From Radio; in the menu that opens, select the port, the radio manufacturer and the required module

![screenshot](images/p10_1.png)

![screenshot](images/p10_2.png)

You will then have two tabs open: the "donor" file and your own radio.

- on the "donor" tab, select the frequencies you need and choose Copy, then switch to the tab of your own radio, select the first row you want to start from and paste the frequencies. *(below is an example of copying data between two incompatible radios, a Baofeng and a Quansheng)* - **this kind of copying is safe, because it copies only the channels (their frequencies, names and settings) and does not affect the general settings of the radio**

![screenshot](images/p10_4.png)

![screenshot](images/p10_3.png)

## 4. FREQUENTLY ASKED QUESTIONS, POSSIBLE PROBLEMS AND SOLUTIONS

**Problems and questions — possible solutions, comments and answers.**

### After installing and configuring the firmware, a frequency cannot be entered in VFO mode

When installing the firmware, the cable MUST be disconnected from the computer before you perform the memory wipe with PTT+EXIT. You have to run the wipe again, then write the calibration data and configure the radio.

### 1. On which frequencies am I allowed to transmit?

There are civil radio frequencies that are allowed for unlicensed use. As a rule these are:

- CB (25.165 – 29.445 MHz) with a TX power of 4.0-12.0 W
- LPD (433.075 – 434.775 MHz) with a TX power of 0.01 W
- PMR (446.00625 – 446.19375) with a TX power of 0.5 W

In some countries the FRS and GMRS bands are used as well.

### 2. On which frequencies am I not allowed to transmit?

Without special permits, transmitting outside the civil bands is prohibited by law. All other frequency bands are used by other services, from radio amateurs to government services, including satellites, cellular networks, air traffic controllers and aircraft, weather stations, river and maritime communications, the military and others. If you interfere with the operation of any of these services, you may be held liable under the laws of your country.

### 3. On which frequencies does the Quansheng UV-K5 receive and transmit?

In the Karina firmware, reception and transmission are open on all bands (see section 2.2, Operating frequency bands).

On radios without hardware modification, transmitting without the risk of burning out the radio is only allowed within the bands declared by the manufacturer: 136-174 MHz / 400-470 MHz.

### 4. What happens if I transmit without an antenna?

Transmitting without an antenna, and also with an antenna tuned for a different frequency band, burns out the output stage of the radio.

### 5. Does the radio transmit on the CB band? Can I talk to truck drivers?

In the Karina firmware the 27 MHz band is open for both reception and transmission by default.

To receive, you need an antenna tuned to this band.

However, transmitting in this band with a radio that has not been modified in hardware does not give usable communication (the output power is far too low). At the same time, because of the physical characteristics of the radio, an attempt to transmit in this band creates interference on the air band and also burns out the output stage of the radio.

### 6. Why can nobody hear me on CB?

In factory condition the TX power of the radio on the CB band does not exceed 0.01 W. Consequently, without physical modification, transmitting in this band is not only useless but also dangerous for the radio itself.

### 7. Why is communication poor inside a car?

The car body shields radio signals. For stable communication it is recommended to fit an external antenna outside the car body.

### 8. Why flash the radio at all?

A stock, out-of-the-box radio works reliably and performs its functions.

Modified firmware extends the functionality of the radio, offering additional and more flexible (professional) settings, higher scanning speed, scanning with a graphical display (spectrum analyser mode) and so on.

### 9. Which firmware is the best?

The one that best suits your needs.

### 10. How do I save the factory firmware?

There is no point in saving the factory firmware, because it is freely available on the internet and on the manufacturer's website. It is far more important to save the original calibration data (which may be unique to your radio) and the configuration file. This is done with the k5prog program.

### 11. The computer does not see the radio when it is connected through the built-in Type-C port

The Type-C port built into the radio is intended for charging the battery only.

Flashing is done with a special programming cable with a KENWOOD-type connector (a cable from analogue Baofeng radios and the like will do).

### 12. Will a Baofeng cable work for flashing and programming?

Yes, it will (one from analogue radios).

### 13. Where do I start flashing?

Any flashing should start with a check of the battery charge. If the battery is charged below 50% (~7.2 V), the flashing process may be faulty or incomplete.

For flashing you need to buy or make a flashing cable with a Kenwood-type connector and install the driver for this cable on the PC.

Prepare the flashing tool. Prepare the firmware file itself. Connect the switched-on radio to the PC with the cable you have bought and use the program to make a backup of your calibration data and of the configuration file. Then connect the radio in flash mode and use the program to write the firmware file.

### 14. Where can I find detailed flashing instructions?

See the section QUICK FLASHING GUIDE FOR THE QUANSHENG UV-K5 AND ITS VARIANTS.

### 15. The computer does not see the radio

- The cable is not pushed all the way into the radio (the first time it goes in very tightly, often until it clicks audibly).
- The cable driver is not installed, or the wrong driver is installed.

### 16. Which program should I use for flashing?

Modified firmware should be flashed as follows:

- the UV-K5, K5(8) and K5+ versions should be flashed with k5prog-win — version 1.26 is recommended;
- the UV-K5+ version (with the Type-C port) should be flashed with k5tools.

### 17. I have flashed the radio, but at power-on it asks for some password

Try all digits the same — 000000 or 111111 — or 123400, or hold MENU+EXIT on the switched-off radio and turn it on without releasing them.

Also, if when configuring through CHIRP or PSCPS you set the side keys FN1 and/or FN2 to NONE (not assigned), the radio may lock and ask for a code at power-on.

If that does not help, wipe the radio's memory with the REBORN firmware — see section 6 of this guide.

### 18. Which program should I use to program (configure) the radio?

CHIRP or PSCPS. To use CHIRP you need to load the module.

### 19. What is CHIRP and what can it do?

It is a program for programming radios. It edits channels and switches various functions on and off, including those that are not available from the radio's own menu.

### 20. I wrote my saved frequencies (from different firmware) or someone else's frequency file, and the radio behaves strangely

Configuration files from different firmware versions can make the radio work incorrectly, which is why writing them is not recommended. Writing other people's configuration and settings files is not recommended either.

If you need to write frequencies from someone else's file (or from your own file, but made with different firmware), use CHIRP: open the other file, read your radio — a second tab will appear — then copy the frequencies you need from the other file's tab and paste them into the tab of your radio. Do not forget to load the appropriate module before reading the files.

### 21. Does the radio have encryption?

The radio has no signal encryption, but it does have a scrambler (voice masking) function. Please note that in many countries the use of encryption, scramblers and other signal-masking functions in civil radio communication is prohibited by law.

### 22. Why does the green LED light up on reception while the speaker stays silent?

- check whether you have receive subtones set (R-DCS and R-CTCS);
- check that both radios use the same modulation (FM in particular).

### 23. What is a subtone?

A subtone is an additional signal, inaudible to the human ear, that is transmitted together with the voice. It acts as a kind of "friend or foe" identifier (by filtering the incoming signal). If a subtone is set, your radio will reject all signals on that frequency and will open for reception only when it detects a signal with the same subtone.

A radio without a subtone, on the other hand, will hear all other radios on reception, both those that use a subtone and those that do not.

### 24. What is the non-standard 55 Hz subtone that the scanner detects?

See the description in the Karina firmware manual, item 22, page 5.

### 25. Why can I hear one correspondent but not the other?

It means that the signal from one operator is strong enough for you to hear him, while the signal from the other is too weak.

This may be due to your antenna not being very efficient, or to one of the operators being closer to you, or simply to the second operator's signal being too weak.

The opposite case is also possible: the signal of one of the correspondents is so strong that it overloads your receiver, which then "chokes" on the excessively strong signal and stays silent.

### 26. I set the radio to scan frequencies, so why do I hear nobody?

To hear someone, you first have to decide where to scan. Scanning "everything at once" will not get you anywhere.

For example, you want to scan the 100-200 MHz range with a 25 kHz step (the scanning speed in frequency (VFO) mode is about 15 frequencies per second), which gives:

100/((0.025)*15)=266 seconds (or almost 5 minutes) for one scanning pass. It is far more efficient to narrow the search range or to start scanning in spectrum analyser mode using the configured presets.

### 27. Can I call for help with the radio?

In exceptional cases, and only **when there is a direct threat to the life and health of people and there is no way to call for help by other technical means of communication**, you may send an SOS or MAYDAY distress signal.

### 28. On which frequencies is it best to call for help so that I am heard?

There are no universally accepted distress frequencies. There are maritime frequencies, river frequencies, mountain emergency frequencies and so on. These frequencies may also differ from region to region and from country to country. When you plan a trip to a particular region, it is advisable at least to find out which emergency communication frequencies are used there.

There are, however, commonly accepted calling frequencies on which you have a better chance of being heard:

- 433.500 — the general calling frequency of the 70 cm band
- 446.09375 — the general calling frequency of the PMR band
- 145.500 — the general calling frequency of radio amateurs (for communication between radio amateurs holding licences and permits)

These frequencies may also differ depending on the region. It is not recommended to occupy them for long conversations. You can always make contact and then move to other frequencies by agreement.

### 29. What is the S symbol that lights up from time to time in the top left corner?

See the description in the Karina firmware manual, item 14, page 5.

### 30. Why, when I change the TX power (or the bandwidth, or the modulation, or the subtone, or the frequency offset), are the changes not saved after switching to another channel and back, or after switching the radio off and on?

See the description in the Karina firmware manual, item 13, page 5.

### 31. When I press PTT the display shows DISABLE — what should I do?

See the description in the Karina firmware manual, items 36 and 37, page 7.

### 32. I have connected a Type-C cable to the radio, but it is not charging

Charging via Type-C is an additional option. It starts at a lower battery voltage and does not charge the battery up to its nominal value. If you can charge the radio in the cradle, use the cradle.

### 33. My radio shows the battery voltage incorrectly — what should I do?

If the battery voltage on the radio's display is implausibly low (~0.25 V) or implausibly high (600 V), that is the first sign that your calibration data is corrupted: you need to write the stock calibration first and only then the Karina calibration.

If that does not help, perform the memory wipe as described in the firmware manual, then install the firmware and the calibration data again.

If the voltage is displayed more or less correctly, with a deviation of about 0.2-0.5 V from the value measured with a multimeter, this is the normal situation with the factory calibration. It can be adjusted in a HEX editor by changing the value of cell 140/6 of the calibration file (in my case this value is B0, but yours may differ).

### 34. Why does the display show 6.0 V while the radio is already switching off?

The operating voltage range of the battery is ~6.0 V - 8.4 V:

- ~8.4 V = 100%
- ~7.2 V = 50%
- ~6.0 V = 0%

Discharging the battery below 4 V leads to its degradation.
