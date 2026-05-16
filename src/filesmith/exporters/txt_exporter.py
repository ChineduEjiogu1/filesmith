from filesmith.utils.file_writer import write_text_file

def save_as_txt(filename, image_object):
    if image_object is None:
        print(f"Error: Cannot save. Image object is None.")
        return False
    
    rows = []
    for y in range(image_object.height):
        row = []
        for x in range(image_object.width):
            pixel = image_object.pixels[y][x]
            r, g, b = pixel
            row.append(f"{r}, {g}, {b}")
        rows.append(" ".join(row))
    
    txt_content = "\n".join(rows)
    
    return write_text_file(filename, txt_content)
