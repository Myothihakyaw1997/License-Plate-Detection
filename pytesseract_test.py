import cv2
import pytesseract
from PIL import Image
import numpy as np


pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
# image = './valid_images/car2.jpg'
image = './images/2.jpg'
img = cv2.imread(image)
# img = cv2.resize(img,(620,480))
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,trans_img = cv2.threshold(np.array(gray_img), 125, 255, cv2.THRESH_BINARY)
trans_img = Image.fromarray(trans_img.astype(np.uint8))

cv2.imshow('img',img)
if cv2.waitKey(0) == 'q':
    cv2.destroyWindow()

def extract_text(img):
    text = pytesseract.image_to_string(img,lang='eng',config='--oem 3 --psm 6')
    return text
txt = extract_text(img = img)
print(txt)
