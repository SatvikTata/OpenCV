import cv2 as cv


#rescaling function
def rescale(img,scale):
    h=int(img.shape[0]*scale)
    w=int(img.shape[1]*scale)
    dim=(w,h)
    return (cv.resize(img,dim,interpolation=cv.INTER_AREA))

scale=float(input("Enter the scale you want: "))

#rescaling the image
#------------------------------------------
img=cv.imread('images/cat_large.jpg')
new_img=rescale(img,scale)
#cv.imshow('cat_large',img)
cv.imshow('cat_resize',new_img)
cv.waitKey(0)

#rescaling the video
#------------------------------------------
#vid=cv.VideoCapture('videos/dog.mp4')
#while(1):
#    isTrue,frame=vid.read()
#    new_frame=rescale(frame)
#    cv.imshow('new_video',new_frame)

#    if(cv.waitKey(20) & 0xFF==ord('d')):
#        break
#vid.release()
#cv.destroyAllWindows()