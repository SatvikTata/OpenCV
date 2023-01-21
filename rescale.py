import cv2 as cv

def changeres(width,height):
    capture.set(3,width)
    capture.set(4,height)

#function for resizing
def resize(frame,scale=0.45):
    height=int(frame.shape[0]*scale)
    width=int(frame.shape[1]*scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

#image part
image=cv.imread('images/cat_large.jpg')
resized_image=resize(image)
cv.imshow('image',image)
cv.imshow('New Image',resized_image)
cv.waitKey(0)


#video part
capture=cv.VideoCapture('videos/dog.mp4')
while True:
    isTrue, frame=capture.read()
    frame_resized=resize(frame)
    #cv.imshow('Video',frame)
    cv.imshow("Resized Video",frame_resized)

    if(cv.waitKey(20) & 0xFF==ord('d')):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)