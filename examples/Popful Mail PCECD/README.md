# Popful Mail English Translation

## Current status  🏗️

 - Translated most of the dialogue text (**needs a rewrite/revision to match the dub and to fit the available space**)
 - Menus partially translated
 - **Only partially tested, there may be crashes!**


## Preview  👀

![shot](https://private-user-images.githubusercontent.com/925171/568058635-bcccf689-aed7-48cc-adc6-dfe768a48e79.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzQ1MzQ5OTYsIm5iZiI6MTc3NDUzNDY5NiwicGF0aCI6Ii85MjUxNzEvNTY4MDU4NjM1LWJjY2NmNjg5LWFlZDctNDhjYy1hZGM2LWRmZTc2OGE0OGU3OS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMzI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDMyNlQxNDE4MTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wNjE2NDZmYjY2MThhOWY5NzcxYjVhNDBlZGVhMTllMTE2YTZlMzYzZjMwODI2ZTA1NzdlZWZkNWU0YTc4YTZlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.1kalA4em12_ER4Nbh8G-13HbjuY92pVOZbM2rWa5n4A)


## Patch instructions  🩹

1. Setup [this hacked PCECD syscard BIOS](https://github.com/eadmaster/ezrominject/wiki/BIOS-font-hacks) in your emulator/flashcart
2. Obtain a disc dump:
   - matching [these hashes](http://redump.org/disc/68156/) for the Jap dub version
   - [wave/iso/cue dump with this patch applied](https://www.romhacking.net/translations/7517/) for the English dub version.
3. Visit [Rom Patcher JS](https://www.marcrobledo.com/RomPatcher.js/), or use an offline xdelta patcher.
4. Select the corresponding ROM file:
   - `PopfulMail (Japan) (Track 02).bin` (Jap dub)
   - `02 Magical Fantasy Adventure - Popful Mail (J).iso` (Eng dub, crc32=`244c18ed`)
5. Download and select the corresponding `.xdelta` as Patch file:
   - `PopfulMail (Japan) (Track 02).bin.xdelta` (Jap dub)
   - `02 Magical Fantasy Adventure - Popful Mail (J).bin.xdelta` (Eng dub)
6. Click "Apply patch" and save in the same folder without changing the filename (same as the input file with `" (patched)"` appended).
7. Download and use the corresponding cue sheet in this folder to play the game:
   - `PopfulMail (English).cue` (Jap dub)
   - `PopfulMail (English)(dub).cue` (Eng dub)
