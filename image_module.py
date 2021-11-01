from PIL import Image
import os.path


class ImageModule:
    def __init__(self):
        pass

    def load_image(self, filepath):
        if os.path.isfile(filepath):
            return Image.open(filepath)
        else:
            print("The file either does not exist or the path is wrong")
