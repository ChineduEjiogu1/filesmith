# Validate width, height, and cell size.
# Create an empty pixel grid.
# Loop through each row.
# Loop through each column.
# Decide which checker cell the pixel belongs to.
# Pick color A or color B.
# Add the pixel to the row.
# Add the row to the grid.
# Return an Image.

from filesmith.core.image import Image

def generate_checkerboard(width, height, cell_size, color_a, color_b):
    if not(width > 0 and height > 0 and cell_size > 0):
        raise ValueError("Dimensions and cell size must be positive integers greater than 0.")
    
    grid = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            cell_x = x // cell_size
            cell_y = y // cell_size

            if (cell_x + cell_y) % 2 == 0:
                grid[y][x] = color_a
            else:
                grid[y][x] = color_b

    my_image = Image(width, height, grid)

    return my_image