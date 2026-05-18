def parse_rgb_color(color_text):
    parts = color_text.split(",")

    if len(parts) != 3:
        raise ValueError("Color must be in the format R,G,B.")
    
    try:
        red, green, blue = map(int, parts)
    except ValueError: 
       raise ValueError("All color values must be valid integers.")


    for value in (red, green, blue):
        if not(0 <= value <= 255):
            raise ValueError("All color values must be between 0 and 255.")
    

    return (red, green, blue)