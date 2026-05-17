# Validate image.
# Get width and height.
# Calculate bytes per pixel.
# Calculate row size before padding.
# Calculate padding per row.
# Calculate row size after padding.
# Calculate pixel data size.
# Calculate full BMP file size.
# Open file in binary mode.
# Write headers.
# Write pixel data bottom-up in BGR order.

import struct

def save_as_bmp(filename, image_object):
    if image_object is None:
        print("Error: Cannot save. Image object is None.")
        return False

    width = image_object.width
    height = image_object.height

    bytes_per_pixel = 3

    row_size_without_padding = width * bytes_per_pixel

    padding = (4 - (row_size_without_padding % 4)) % 4

    row_size_with_padding = row_size_without_padding + padding

    pixel_data_size = row_size_with_padding * height

    file_size =  14 + 40 + pixel_data_size


    with open(filename, 'wb') as f:
        f.write(b'BM')                        # magic bytes
        f.write(struct.pack('<I', file_size)) # total file size
        f.write(struct.pack('<H', 0))         # reserved
        f.write(struct.pack('<H', 0))         # reserved
        f.write(struct.pack('<I', 54))        # offset to pixel data (14 + 40)

        f.write(struct.pack('<I', 40))         # DIB header size
        f.write(struct.pack('<i', width))      # image width
        f.write(struct.pack('<i', height))     # image height
        f.write(struct.pack('<H', 1))          # color planes
        f.write(struct.pack('<H', 24))         # bits per pixel (RGB)
        f.write(struct.pack('<I', 0))          # no compression
        f.write(struct.pack('<I', pixel_data_size)) # pixel data size
        f.write(struct.pack('<i', 0))          # pixels per meter X
        f.write(struct.pack('<i', 0))          # pixels per meter Y
        f.write(struct.pack('<I', 0))          # colors in table
        f.write(struct.pack('<I', 0))          # important colors

        for y in range (height -1, -1, -1):
            for x in range(width):
                r, g, b= image_object.pixels[y][x]
                f.write(bytes([b, g, r]))

            f.write(b'\x00' * padding)

    print(f"Successfully saved BMP image to {filename}")

    return True