def save_as_txt(filename, image_object):
    if image_object is None:
        print(f"Error: Cannot save. Image object is None.")
        return False
    
    with open(filename, 'w') as f:
        for y in range(image_object.height):
            row = []
            for x in range(image_object.width):
                pixel = image_object.pixels[y][x]
                r, g, b = pixel
                row.append(f"{r}, {g}, {b}")
            f.write(" ".join(row))
            if y < image_object.height - 1:
                f.write("\n")

    return True