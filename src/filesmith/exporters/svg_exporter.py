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

def save_as_svg(filename, image, cell_size):
    if image is None or (cell_size <= 0):
        return False

    svg_content = f'<svg width="{image.width * cell_size}" height="{image.height * cell_size}" xmlns="http://www.w3.org/2000/svg">\n'

    for y in range(image.height):
        for x in range(image.width):
        # append each <rect> to svg_content
            cell_x = x * cell_size
            cell_y = y * cell_size
            r, g, b = image.pixels[y][x]

            svg_content += (f'<rect x="{cell_x}" y="{cell_y}" width="{cell_size}" height="{cell_size}" fill="rgb({r},{g},{b})"/>\n')


    svg_content += '</svg>\n'

    return write_text_file(filename, svg_content)