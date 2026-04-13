
INPUT_ROM="Star Hearts - Hoshi to Daichi no Shisha (Japan).wsc"
OUTPUT_ROM="Star Hearts - Hoshi to Daichi no Shisha (English).wsc"

cp "$INPUT_ROM" "$OUTPUT_ROM"

python ../../ezrominject.py *_jap.txt *_eng.txt "$OUTPUT_ROM"
# TODO: patch internal font and use --ascii-bios-hack
# --abbreviate
# NOT SUPPORTED: --ascii-mode

#xdelta3 -S none -f -e -s "$INPUT_ROM" "$OUTPUT_ROM"  "$OUTPUT_ROM.xdelta"



