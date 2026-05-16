def generate_report(project):
    lines = [
        "Project:",
        f"  title: {project.title}",
        f"  description: {project.description}",
        f"  image: {project.image}",
        f"  created_at: {project.created_at}",
        "  generated_files:",
    ]
    for path in project.generated_files:
        lines.append(f"    - {path}")

    return "\n".join(lines)

def save_report(project, filename):
    """Generates a structured text analysis report and raw grid mapping from a Project."""
    # 1. Verify project exists and extract the real image object
    if project is None or project.image is None:
        print("Error: Cannot save. Project or project image is None.")
        return False
        
    image_object = project.image

    with open(filename, 'w') as f:
        # Write high-level metadata headers
        f.write("========================================\n")
        f.write(f"  FILESMITH REPORT: {project.title.upper()} \n")
        f.write("========================================\n\n")
        
        # No extra import needed! project.created_at is already a datetime object.
        formatted_time = project.created_at.strftime("%Y-%m-%d %I:%M %p")
        f.write(f"Created At:   {formatted_time}\n")
        f.write(f"Dimensions:   {image_object.width} x {image_object.height} pixels\n\n")
        
        f.write("--- DESCRIPTION ---\n")
        f.write(f"{project.description or 'No description provided.'}\n\n")
        
        f.write("--- GENERATED FILE MANIFEST ---\n")
        for path in project.generated_files:
            f.write(f"- {path}\n")
        f.write(f"- {filename} (This Report File)\n\n")

        # Your custom pixel matrix visualization loop
        f.write("--- RAW PIXEL GRID MAP ---\n")
        for y in range(image_object.height):
            row = []
            for x in range(image_object.width):
                pixel = image_object.pixels[y][x]
                r, g, b = pixel
                row.append(f"({r},{g},{b})")
                
            f.write(" ".join(row))
            f.write("\n")
            
        f.write("\n========================================\n")
        f.write("Report compiled successfully.\n")

    print(f"Successfully saved text report to {filename}")
    return True
    
    


def print_report(project):
    print(generate_report(project))
