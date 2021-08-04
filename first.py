import cv2

img = cv2.imread('lena.jpg', 1)
##
cv2.imshow('image', img)
print("First image is shown in the screen:")
print(img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('lena_copy.png', img)


img2 = cv2.imread('lena_copy.png', -1)
cv2.imshow('image', img2)
print("the second image is poped down in the window:")
print(img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


