import os

FONT_PATH = "spleen-6x12.psfu"
OUTPUT_PATH = "spleen-6x12_lc_font.dat"

# 12x12 Font Configuration Offsets
FONT_UPPER_A = 0x32C       
FONT_LOWER_A = 0x4AC       

def get_glyph(font_data, char_code):
    if ord('A') <= char_code <= ord('Z'):
        offset = FONT_UPPER_A + (char_code - ord('A')) * 12
    elif ord('a') <= char_code <= ord('z'):
        offset = FONT_LOWER_A + (char_code - ord('a')) * 12
    else:
        return b'\x00' * 12
    return font_data[offset : offset + 12]

def generate_lc_font():
    if not os.path.exists(FONT_PATH):
        print(f"Error: {FONT_PATH} not found.")
        return

    with open(FONT_PATH, "rb") as f:
        font_data = f.read()

    letters = [chr(i) for i in range(ord('A'), ord('Z')+1)] + \
              [chr(i) for i in range(ord('a'), ord('z')+1)] + \
              [" "]

    records = []
    sjis_value = 0x889F 

    for char1 in letters:
        for char2 in letters:
            b1, b2 = divmod(sjis_value, 256)
            header = bytes([b1, b2])
            
            glyph1 = get_glyph(font_data, ord(char1))
            glyph2 = get_glyph(font_data, ord(char2))
            
            bitmap = bytearray()
            for i in range(16):
                if i < 12:
                    # Spleen 6x12 usually sits in the top 6 bits (7-2)
                    bits1 = (glyph1[i] >> 2) & 0x3F 
                    bits2 = (glyph2[i] >> 2) & 0x3F

                    # REDUCING GAP TO 1PX VISUAL:
                    # Old shift (3) gave 2px visual. 
                    # New shift (4) overlaps the 1px font-padding to give 1px visual.
                    bigram_row = (bits1 << 10) | (bits2 << 4)
                    
                    # Apply 1px LEFT padding (shifts entire bigram 1 bit right)
                    final_row = (bigram_row >> 1) & 0xFFFF
                    
                    out_row1 = (final_row >> 8) & 0xFF
                    out_row2 = final_row & 0xFF
                else:
                    out_row1 = out_row2 = 0x00
                
                # Space Guard for NitroPaint
                if char1 == " " and i == 15: out_row1 |= 0x80
                if char2 == " " and i == 15: out_row2 |= 0x01
                        
                bitmap.append(out_row1)
                bitmap.append(out_row2)
            
            header_int = (b1 << 8) | b2
            records.append((header_int, header + bitmap))
            
            # SJIS Pointer increment
            trail = sjis_value & 0xFF
            lead = sjis_value >> 8
            trail += 1
            if trail == 0x7F: trail = 0x80
            elif trail > 0xFC: trail = 0x40; lead += 1
            sjis_value = (lead << 8) | trail 

    records.sort(key=lambda x: x[0])
    with open(OUTPUT_PATH, "wb") as out_file:
        for _, data in records:
            out_file.write(data)

    print(f"Done! Created {OUTPUT_PATH} with narrowed internal spacing.")

if __name__ == "__main__":
    generate_lc_font()