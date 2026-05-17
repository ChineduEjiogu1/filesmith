from filesmith.core.image import Image

def generate_gradient(width, height, color_a, color_b, direction):

    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be greater than 0.")
    
    # Validate direction
    if direction not in ['horizontal', 'vertical']:
        raise ValueError("Direction must be 'horizontal' or 'vertical'.")
    
    grid = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            # Calculate interpolation factor 't' based on direction
            if direction == 'horizontal':
                # Handle single-pixel width to avoid division by zero
                t = x / (width - 1) if width > 1 else 0.0
            else:
                # Handle single-pixel height to avoid division by zero
                t = y / (height - 1) if height > 1 else 0.0

            # Linearly interpolate each RGB channel
            r = color_a[0] + t * (color_b[0] - color_a[0])
            g = color_a[1] + t * (color_b[1] - color_a[1])
            b = color_a[2] + t * (color_b[2] - color_a[2])

            # Assign the color to the specific pixel in the grid
            grid[y][x] = int(r), int(g), int(b)

    return Image(width, height, grid)