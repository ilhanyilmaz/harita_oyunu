import cv2
import numpy as np
from random import randint

image = cv2.imread("./il_sinirlari.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
r,threshold = cv2.threshold(gray,220,255,cv2.THRESH_BINARY_INV)
cv2.imshow('threshold',threshold)
contours, hierarcy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


i=0
for contour in contours:
    width, height = gray.shape
    x,y,w,h = cv2.boundingRect(contour)
    mask = np.zeros((width,height),np.uint8)

    cv2.drawContours(image,contours,i,(randint(0,255),randint(0,255),randint(0,255)),1)
    cv2.drawContours(mask, [contour], 0, 255, -1)
    city = mask[y:y+h,x:x+w]
    cv2.imshow('city', city)
    if cv2.waitKey(10) != -1:
        break
    i+=1

cv2.imshow('sinirlar', image)

if cv2.waitKey(0) != -1:
    cv2.destroyAllWindows()
