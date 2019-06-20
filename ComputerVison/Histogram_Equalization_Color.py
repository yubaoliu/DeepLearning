import cv2
import numpy as np

img = cv2.imread('../../Assets/Images/senn01.jpeg', 1)

cv2.imshow('src', img)

(b, g, r) = cv2.split(img)

bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)

result = cv2.merge((bH, gH, rH))

cv2.imshow('dst', result)
cv2.waitKey(0)