import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import tensorflow as tf

IMAGE_PATH = 'payment.png'

reader = easyocr.Reader(['en'])
output = reader.readtext(IMAGE_PATH)

for (bbox, text, prob) in output:
    text = "".join ([c if ord(c)<128 else "" for c in text])
    print (text)