## Overview

This is a text/code companion for [my YouTube video on using Tesseract OCR from Python](#).

If you would like a visual walkthrough and explanation, you can [watch the video](#).

# Setup

You must have Tesseract downloaded and installed on your machine: https://github.com/tesseract-ocr/tesseract

You must have python3 downloaded and installed on your machine: https://www.python.org/downloads/

# Usage

1. Run `pip3 install -r ./requirements.txt` to install pytesseract
2. Update [simple-tesseract-example.py](./simple-tesseract-example.py) or [all-png-in-dir.py](./all-png-in-dir.py) with the proper path for your directory structure.
3. Running
    - Run `python3 ./simple-tesseract-example.py` to extract text from the specified image file
    
    OR
    - Run `python3 ./all-png-in-dir.py` to extract text from all png files in the specified directory
