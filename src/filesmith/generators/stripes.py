from filesmith.core.image import Image

def generate_stripes(width, height, stripe_size, color_a, color_b, direction):
    
    if width <= 0 or height <= 0 or stripe_size <= 0:
        raise ValueError("Dimensions and stripe size must be positive integers greater than 0.")
    
    valid_directions = ('vertical', 'horizontal')

    if direction not in valid_directions:
        raise ValueError(f"Direction must be one of {valid_directions}.")

    grid = [[0 for _ in range(width)] for _ in range(height)]

    if direction == 'vertical':
        for x in range(width):
            stripe_number = x // stripe_size
            color = color_a if stripe_number % 2 == 0 else color_b

            for y in range(height):
                grid[y][x]= color

    elif direction == "horizontal":
        for y in range(height):
            stripe_number = y // stripe_size
            color = color_a if stripe_number % 2 == 0 else color_b

            for x in range(width):
                grid[y][x] = color
    
    return Image(width, height, grid)