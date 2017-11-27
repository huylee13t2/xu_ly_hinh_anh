from PIL import Image
import cv2, sys, os, pytesseract
import numpy as np
from matplotlib import pyplot as plt
 

image = cv2.imread("ex2.png")
mser = cv2.MSER_create()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

 
# xu ly hinh anh
# gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# gray = cv2.GaussianBlur(gray, (3, 3), 0)
# gray = cv2.medianBlur(gray, 3)
# gray = cv2.Canny(gray, 10, 250)

vis = image.copy()
regions, _ = mser.detectRegions(gray)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
cv2.polylines(vis, hulls, 1, (0, 255, 0))
cv2.imshow('img', vis)

# ve cac contours
mask = np.zeros((image.shape[0], image.shape[1], 1), dtype=np.uint8)
for contour in hulls:
    cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)

text_only = cv2.bitwise_and(image, image, mask=mask)


# su dung bo loc
gray = cv2.GaussianBlur(gray,(3,3),0)
# gray = cv2.bilateralFilter(gray,9,75,75)
cv2.imshow('Filter', gray)



# luu hinh anh gray
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# xac dinh van ban
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print('Result : ')
print(text)
 
cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)