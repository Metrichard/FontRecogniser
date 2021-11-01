import image_module

file_path = r"../FontRecogniser/TestPictures/test_picture.jpg"

imageLoader = image_module.image_module(file_path)
imageLoader.invert_colours_of_image()

imageLoader.stored_image.show()
