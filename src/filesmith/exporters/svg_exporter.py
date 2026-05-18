# Check that the project or image exists.
# Open the SVG file.
# Write the SVG opening tag with width and height.
# Loop through checkerboard cells.
# Write one rectangle for each cell.
# Close the SVG tag.


# Check that image exists and cell_size is valid.
# Open the output SVG file.
# Write the SVG opening tag using image width and height.
# Loop through checkerboard cells using steps of cell_size.
# Decide the cell color.
# Convert the RGB tuple to an SVG color string.
# Write one rectangle for the cell.
# Close the SVG tag.
# Return success.

from filesmith.utils.file_writer import write_text_file

def save_as_svg(filename, image, scale):
    if image is None:
        print("Error: Image is missing.")
        return False

    if scale <= 0:
        print("Error: Scale must be greater than 0.")
        return False
    
    svg_width = image.width * scale
    svg_height = image.height * scale

    svg_content = f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width}" height="{svg_height}">\n'

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.pixels[y][x]
            rec_x = x * scale
            rec_y = y * scale
            svg_content += f'<rect x="{rec_x}" y="{rec_y}" width="{scale}" height="{scale}" fill="rgb({r},{g},{b})"/>\n'

    svg_content += '</svg>\n'

    return write_text_file(filename, svg_content)