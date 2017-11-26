from PIL import Image
import pytesseract
import cv2
import os
 

image = cv2.imread("ex2.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# xu ly hinh anh
# gray = cv2.GaussianBlur(gray, (3, 3), 0)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# gray = cv2.medianBlur(gray, 3)
# gray = cv2.Canny(gray, 10, 250)

 
 
# luu hinh anh gray
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# xac dinh van ban
text = pytesseract.image_to_string(Image.open(filename))
# os.remove(filename)
print(text)
 
cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)