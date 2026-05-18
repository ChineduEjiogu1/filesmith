from filesmith.core.image import Image

def scale_image_nearest(image, scale):
    if image is None:
        print("Error: Image is None.")
        return None

    if scale <= 0:
        print("Error: Scale must be greater than 0.")
        return None

    new_width = image.width * scale
    new_height = image.height * scale

    new_grid = []

    for y in range(image.height):
        for _ in range(scale):
            new_row = []
            for x in range(image.width):
                pixel_color = image.pixels[y][x]
                for _ in range(scale):
                    new_row.append(pixel_color)
            new_grid.append(new_row)

    return Image(new_width, new_height, new_grid)