import cv2 as cv

img=cv.imread("images/park.jpg")
cv.imshow("Park",img)
print(img.shape)

#resizing the image
resize=cv.resize(img,(1700,400),interpolation=cv.INTER_CUBIC)
cv.imshow("Resized",resize)
print(resize.shape)

#cropping the image
cropped=img[150:427,200:640]
cv.imshow("cropped",cropped)

#converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GrayScale",gray)

#blurring the image
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#edge cascade
edge=cv.Canny(blur,125,175)
cv.imshow("Edge Image",edge)

#dilating the image
dilated =cv.dilate(edge,(7,7),iterations=3)
cv.imshow("Dilated",dilated)

#eroding the image
eroded =cv.erode(dilated,(7,7),iterations=3)
cv.imshow("Eroded",eroded)

cv.waitKey(0)