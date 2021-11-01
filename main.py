from image_module import ImageModule

file_path = r"../FontRecogniser/TestPictures/test_picture.jpg"

imageLoader = ImageModule()

image = imageLoader.load_image(file_path)

image.show()
