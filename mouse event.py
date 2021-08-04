# import numpy as np
# import cv2
#
# # event = [i for i in dir(cv2) if 'EVENT' in i]
# # print(event)
#
# def clickevent(event, x, y, flag, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x,'  ', y)
#         font = cv2.FONT_HERSHEY_COMPLEX
#         strg = str(x) + ', ' + str(y)
#         cv2.putText(img, strg, (x,y), font, 1, (255,255,0), 1)
#         cv2.imshow('image', img)
#     # elif(event == cv2.EVENT_RBUTTONDOWN): // For the event of right click button.
#     #     print(x, ' ', y)
#     #     font = cv2.FONT_HERSHEY_COMPLEX
#     #     strg = str(x) + ', ' + str(y)
#     #     cv2.putText(img, strg, (x,y), font, 1, (0,255,0), 1)
#     #     cv2.imshow('image', img)
#     elif(event == cv2.EVENT_RBUTTONDOWN):
#         blue = img[y, x, 0]
#         green = img[y, x, 1]
#         red = img[y, x, 2]
#         font = cv2.FONT_HERSHEY_COMPLEX
#         strg = str(blue) + ', ' + str(green) + ', ' + str(red)
#         cv2.putText(img, strg, (x,y), font, 1, (255,255,255), 1)
#         cv2.imshow('image', img)
#
# img = cv2.imread('lena.jpg')
# cv2.imshow('image', img)
#
# # img = np.zeros((512, 512, 3), np.uint8)  // Method for creating black image
# # cv2.imshow('image', img)
#
# cv2.setMouseCallback('image', clickevent)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import numpy as np
import cv2
#
# def click_event(event, x, y, flag, param):
#     # if (event == cv2.EVENT_LBUTTONDOWN):
#     #     cv2.circle(img, (x,y), 3, (0, 0, 255), -1)
#     #     points.append((x, y))
#     #     if len(points) >= 2:
#     #         cv2.line(img, points[-1], points[-2], (255, 0, 255), 3)
#     #     cv2.imshow('image', img)

#     if event == cv2.EVENT_LBUTTONDOWN:
#         blue = img[x,y,0]
#         green = img[x,y,1]
#         red = img[x,y,2]
#         cv2.circle(img, (x, y), 3, (0,0,255), -1)
#         mycolorImage = np.zeros((512,512, 3), np.uint8)
#
#         mycolorImage[:] = [blue, green, red]
#         cv2.imshow('color', mycolorImage)
#
# #img = np.zeros((512,512,3), np.uint8)
# img = cv2.imread('lena.jpg')
# cv2.imshow('image', img)
# points = []
# cv2.setMouseCallback('image', click_event)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import numpy as np
import cv2

# event = [i for i in dir(cv2) if 'EVENT' in i]
# print(event)

def clickevent(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,'  ', y)
        font = cv2.FONT_HERSHEY_COMPLEX
        strg = str(x) + ', ' + str(y)
        cv2.putText(img, strg, (x,y), font, 1, (255,255,0), 1)
        cv2.imshow('image', img)

img = cv2.imread('messi5.jpg')
cv2.imshow('image', img)
cv2.setMouseCallback('image', clickevent)

cv2.waitKey(0)
cv2.destroyAllWindows()

