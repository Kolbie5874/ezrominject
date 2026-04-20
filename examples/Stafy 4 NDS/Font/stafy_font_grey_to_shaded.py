import struct
import os

# --- Configuration ---
INPUT_FILE = "stafy4_13b2_full_bmp_comb_clean.bin.spleen"
OUTPUT_FILE = "stafy4_13b2_full_bmp_comb_clean.bin"

BLACK_INDEX = 1  # The color for the core text
WHITE_INDEX = 2  # The color for the grey shadow

def convert_with_exceptions():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    with open(INPUT_FILE, "rb") as f:
        data = bytearray(f.read())

    cell_height = data[0]
    depth = data[1]
    n_table = struct.unpack('<H', data[2:4])[0]
    depth_mask = (1 << depth) - 1
    
    table_offset = 4
    ofs_placeholder = n_table * 4 + 4
    
    # Map offsets to Code Points
    target_map = {}
    for i in range(n_table):
        offs = struct.unpack('<I', data[table_offset + i * 4 : table_offset + i * 4 + 4])[0]
        if offs == 0 or offs == ofs_placeholder or offs >= len(data):
            continue
            
        if n_table == 0x3000:
            hi = i // 0xC0
            lo = (i % 0xC0) + 0x40
            cp = 0x8000 + lo + (hi << 8)
        else:
            cp = i
        
        # Target Range + Space
        if (0x889F <= cp <= 0x9792) or cp == 0x20:
            target_map[offs] = cp

    print(f"Processing {len(target_map)} glyphs with specific padding rules...")

    for offs, cp in target_map.items():
        orig_width = data[offs]
        stride = data[offs + 1]
        
        # --- Logic Branching ---
        # Exception range: No left padding (no x-shift)
        is_exception = (0x975E <= cp <= 0x9792)
        
        if is_exception:
            new_width = orig_width + 1  # Only need room for shadow logic
            shift_x = 0
        else:
            new_width = orig_width + 2  # Room for 1px shift + 1px margin
            shift_x = 1

        # Stride safety check
        if (new_width * depth) > (stride * 8):
            new_width = (stride * 8) // depth
            
        data[offs] = new_width

        # 1. Extract Original Grid
        grid = [[0 for _ in range(orig_width)] for _ in range(cell_height)]
        for y in range(cell_height):
            row_start = offs + 2 + (stride * y)
            for x in range(orig_width):
                bitaddr = x * depth
                pxval = (data[row_start + (bitaddr // 8)] >> (bitaddr % 8)) & depth_mask
                grid[y][x] = pxval

        # 2. Build Output Grid
        out_grid = [[0 for _ in range(new_width)] for _ in range(cell_height)]
        
        for y in range(cell_height):
            for x in range(orig_width):
                if grid[y][x] > 0:
                    tx = x + shift_x
                    if tx < new_width:
                        # Draw Core Text
                        out_grid[y][tx] = BLACK_INDEX
                        
                        # Draw Shadow Strictly Below
                        if y + 1 < cell_height:
                            out_grid[y+1][tx] = WHITE_INDEX

        # 3. Repack Bits
        for y in range(cell_height):
            row_start = offs + 2 + (stride * y)
            for b in range(stride): data[row_start + b] = 0 # Clear row
            
            for x in range(new_width):
                val = out_grid[y][x]
                bitaddr = x * depth
                byte_idx = row_start + (bitaddr // 8)
                if byte_idx < row_start + stride:
                    data[byte_idx] |= (val << (bitaddr % 8))

    with open(OUTPUT_FILE, "wb") as f:
        f.write(data)

    print("Done! Exceptions applied to 0x975E-0x9792 (no left shift).")

if __name__ == "__main__":
    convert_with_exceptions()