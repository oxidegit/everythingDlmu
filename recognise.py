# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
import sys
import pytesseract


if __name__ == "__main__":
    print(pytesseract.image_to_string(Image.open('a.gif'), lang='eng'))