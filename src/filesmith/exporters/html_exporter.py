# This file exports a Project object as an HTML report.
# Check that the project exists.
# Pull image details from the project.
# Build the HTML document.
# List generated files.
# Save the HTML to disk.
# Return success or failure.

'''
check project exists
check project has image
build HTML text
open .html file
write HTML text
return success/failure
'''

from filesmith.utils.file_writer import write_text_file

def save_report_html(filename, project_object):
    if project_object is None:
        print("Error: Cannot save. Project is None.")
        return False

    if project_object.image is None:
        print("Error: Cannot save. Project has no image.")
        return False
    
    image = project_object.image

    total_pixels = image.width * image.height

    color_counts = {}

    for row in image.pixels:
        for pixel in row:
            if pixel not in color_counts:
                color_counts[pixel] = 1
            else:
                color_counts[pixel] += 1

    color_rows = ""
    
    for color, count in color_counts.items():
        percentage = (count / total_pixels) * 100
        color_rows += f"<li>{color}: {count} pixels ({percentage:.1f}%)</li>\n"


    files_html = ""

    if project_object.generated_files:
        for file in project_object.generated_files:
            files_html += f"<li>{file}</li>\n"
    else:
        files_html = "<li>No files generated yet</li>"
    

    html_content = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{project_object.title}</title>
    </head>
    <body>
        <h1>{project_object.title}</h1>
        <p>description: {project_object.description}</p>
        <p>created_at: {project_object.created_at}</p>

        <h2>Image Details</h2>
        <ul>
            <li><strong>Width:</strong> {image.width}px</li>
            <li><strong>Height:</strong> {image.height}px</li>
            <li><strong>Total Pixels:</strong> {total_pixels:,}</li>
        </ul>
        <h2>Color Distribution</h2>
        <ul>
{color_rows}        </ul>

        <h2>Generated Files</h2>
        <ul>
{files_html}        </ul>
    </body>
    </html>"""

    return write_text_file(filename, html_content)