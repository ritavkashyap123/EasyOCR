import easyocr
import cv2
import numpy as np

IMAGE_PATH = 'surf.png'

reader = easyocr.Reader(['en'])
result = reader.readtext(IMAGE_PATH)
result
