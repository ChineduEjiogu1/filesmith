# This file defines the image data structure used by FileSmith.

'''Image constructor:
- stores width
- stores height
- stores the full pixel grid

validate_position:
- receives x and y
- checks x against width
- checks y against height
- returns valid/invalid

get_pixel:
- receives x and y
- validates the position
- returns the color at pixels[y][x]

set_pixel:
- receives x, y, and new color
- validates the position
- changes pixels[y][x]
'''

class Image:

    def __init__(self, width, height, pixels):
        self.width = width # x = column = width
        self.height = height # y = row = height
        self.pixels = pixels
        
        if not self.validate_pixels():
            raise ValueError("Invalid pixel data provided for Image initialization.")

    def validate_position(self, x, y):
        if not (0 <= x < self.width):
            print(f"X position {x} is out of bounds (0 to {self.width-1})")
            return False
        if not (0 <= y < self.height):
            print(f"Y position {y} is out of bounds (0 to {self.height-1})")
            return False
        
        return True

    def get_pixel(self, x, y):
        if self.validate_position(x, y):
            return self.pixels[y][x]
        return None

    def set_pixel(self, x, y, new_color):
        if self.validate_position(x, y):
            self.pixels[y][x] = new_color

    def validate_pixels(self):
        if not (self.width > 0 and self.height > 0):
            print(f"Invalid dimensions: {self.width}x{self.height}")
            return False
        
        if len(self.pixels) != self.height:
            print(f"Invalid height: Expected {self.height}, got {len(self.pixels)}")
            return False
        
        invalid_rows = [
            i for i, row in enumerate(self.pixels) 
            if len(row) != self.width
        ]
        # Assuming 'pixels' is a list of lists and 'width' is the target length
        if invalid_rows:
            print(f"Invalid pixel row width at indices: {invalid_rows}")
            return False
        
        return True