def write_text_file(filename, content):
    if not filename:
        print(f"Error: Filename is missing or empty")
        return False
    
    if content is None:
        print(f"Error: Cannot write to '{filename}'. Content is None.")
        return False

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Successfully wrote content to {filename}")
    return True