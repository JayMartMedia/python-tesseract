from PIL import Image

import pytesseract

# Replace with your path
print(pytesseract.image_to_string(Image.open('C:/Users/{username}/{path}}/test-image.png')))
