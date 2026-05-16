# This file exports an Image object as a PPM file.

# Open the output file.
# Write the PPM format line.
# Write the image width and height.
# Write the max color value.
# Loop through each row.
# Loop through each pixel in the row.
# Write the RGB values.

def save_as_ppm_p3(filename, image_object):
    if image_object is None:
        print(f"Error: Cannot save. Image object is None")
        return False  # Stops the function right here

    with open(filename, 'w') as f:
        f.write("P3\n")
        f.write(f"{image_object.width} {image_object.height}\n")
        f.write("255\n")

        for y in range(image_object.height):
            row = []
            for x in range(image_object.width):
                pixel = image_object.pixels[y][x]
                r, g, b = pixel
                row.append(f"{r} {g} {b}")
            f.write(" ".join(row))
            if y < image_object.height - 1:
                f.write("\n")

    print(f"Successfully saved image to {filename}")

    return True


def save_as_ppm_p6(filename, image_object):
    """Saves the image in compressed binary (P6) format."""
    if image_object is None:
        print("Error: Cannot save. Image object is None.")
        return False  

    with open(filename, 'wb') as f:
        # 1. Write the P6 header as raw bytes
        f.write(b"P6\n")
        
        # 2. FIX: Added the critical \n at the end of the dimensions line
        header_dimensions = f"{image_object.width} {image_object.height}\n"
        f.write(header_dimensions.encode('ascii'))
        
        # 3. Write the max color value
        f.write(b"255\n")
        
        # 4. Stream the raw pixel bytes
        for y in range(image_object.height):
            for x in range(image_object.width):
                r, g, b = image_object.pixels[y][x]
                # Called as a function with parentheses, passing a list!
                f.write(bytes([r, g, b]))
                
    print(f"Successfully saved binary P6 image to {filename}")
    
    return True