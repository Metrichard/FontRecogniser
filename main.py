import image_module

file_path = r"../FontRecogniser/TestPictures/test_picture.png";

imageLoader = image_module.image_module()

image = imageLoader.load_image(file_path)

image.show()