import easyocr
import cv2
import re

num = 14
img = cv2.imread(f'./invalid_images/car{num}.jpg')
# cv2.imshow('img',img)
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.waitKey(0)
cv2.destroyAllWindows()

''' download english text library '''
reader = easyocr.Reader(['en'])
# txts = reader.readtext(f'./invalid_images/car{num}.jpg')
txts = reader.readtext(grey)
raw_str =''.join([i[-2] for i in txts])
licence_reg = r"\d[a-zA-Z]\s*[-:=\/]*\s*\d{4}"
if re.search(licence_reg,raw_str):
    license = re.search(licence_reg,raw_str).group()
    print(license)
else:
    print('no license detected')
    print(raw_str)