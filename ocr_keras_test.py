import keras_ocr
import cv2
import numpy as np

pipepline = keras_ocr.pipeline.Pipeline()
img = keras_ocr.tools.read('./images/1.jpeg')
# print(img)
img = np.array(img).reshape((3,2))
# img = cv2.imread('./images/2.jpg')
text = pipepline.recognize(img)
print(text)