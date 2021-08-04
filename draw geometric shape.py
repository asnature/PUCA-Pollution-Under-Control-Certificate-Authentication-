import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)## This method is used to generate the blank black image.

img = cv2.imread('lena.jpg', 1)
img = cv2.line(img, (0,0), (255, 255),(0,0,255), 3)
img = cv2.arrowedLine(img, (0,10), (355, 355),(0,255,0), 3)
img = cv2.rectangle(img, (200,200), (370,370), (0,0,255),5)
img = cv2.circle(img, (285,285), (90),(255,0,0),3)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, "face", (270,270), font, 1, (255,255,255), 2, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()