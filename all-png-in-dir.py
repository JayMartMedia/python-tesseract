from pathlib import Path
from PIL import Image
import pytesseract

# Replace with your path
directory = 'C:/Users/{username}/{path}'

files = Path(directory).glob('*.png')
for file in files:
    print(file)
    print(pytesseract.image_to_string(Image.open(file)))
    print('\n----------\n')
