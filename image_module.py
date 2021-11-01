from PIL import Image
import os.path


class ImageModule:
    def __init__(self, filepath):
        self.stored_image = None
        if os.path.isfile(filepath):
            self.stored_image = Image.open(filepath)
        else:
            print("The file either does not exist or the path is wrong")

    def get_stored_image(self):
        return self.stored_image

    def invert_colours_of_image(self):
        if self.stored_image:
            width, height = self.stored_image.size
            for x in range(width):
                for y in range(height):
                    r, g, b, _ = self.stored_image.getpixel((x, y))
                    if r < 30 and g < 30 and b < 30:
                        self.stored_image.putpixel((x, y), (255, 255, 255))
                    else:
                        self.stored_image.putpixel((x, y), (0, 0, 0))
