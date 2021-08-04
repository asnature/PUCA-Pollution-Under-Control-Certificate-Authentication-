import cv2

img = cv2.imread('messi5.jpg')
#img2 = cv2.imread('opencv-logo.png')


print(img.shape)# // Return a tuple of number of rows, columns, and channels.
print(img.size)# // Return Total number of pixel in the image.
print(img.dtype)# // Return the data type the image obtained.
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

# ball = img[280:340, 330:390]
# img[273:333, 100:160] = ball
# ball = img[67:196, 135:267]
# img[67+100:196+100, 135+100:267+100] = ball
# ball = img[286:325, 334:396]
# img[273:333, 100:160] = ball
ball = img[284:392, 335:324]
img[284-50:392-50, 335-35:324-35] = ball

# img = cv2.resize(img, (512,512))
# img2 = cv2.resize(img2, (512,512))
#
# dst = cv2.add(img, img2);


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()