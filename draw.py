import cv2 as cv
import numpy as np

b=int(input("Give the value of blue (0-255): "))
g=int(input("Give the value of green (0-255): "))
r=int(input("Give the value of red (0-255): "))

blank=np.zeros((500,500,3),dtype='uint8')
#cv.imshow('No image',blank)

#blank[200:300,200:300]=0,255,0
#cv.imshow('Green Image',blank)

cv.rectangle(blank,(blank.shape[0]//4,blank.shape[1]//4),(blank.shape[0]*3//4,blank.shape[1]*3//4),(255,0,0),thickness=-1)
#cv.imshow("Blue Rectangle",blank)

cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),172,(b,g,r),thickness=3)
#cv.imshow('Circle',blank)

cv.line(blank,(70,70),(140,140),(0,0,255),thickness=10)
#cv.imshow('Image',blank)

cv.putText(blank,"Hello Humans!!",(25,400),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
cv.imshow('Text',blank)

cv.waitKey(0)