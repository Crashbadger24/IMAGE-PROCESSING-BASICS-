import cv2 as cv
def frame_scaler(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)
img = cv.imread(r"D:\python\Learning_ML\Imageprocessing\ImagesandVideos\WhatsApp Image 2024-05-28 at 16.21.06_4b37df10.jpg")

#Grayscale
grayscale = cv.cvtColor(frame_scaler(img,scale=0.5),cv.COLOR_BGR2GRAY)
cv.imshow('GREYSCALE',grayscale)

#BlurImage the tuple should have both odd numbers 
blurred = cv.GaussianBlur(frame_scaler(img,scale=0.5),(3,3),cv.BORDER_CONSTANT)
cv.imshow('Blurred',blurred)

#Canny edge detection
canny = cv.Canny(blurred,125,175)
cv.imshow('Canny',canny)

#Dilating an image
dilating = cv.dilate(canny,(11,11),iterations=4)
cv.imshow('dilated',dilating)

#Eroding an image
eroded = cv.erode(dilating,(3,3),iterations=4)
cv.imshow("Eroded",eroded)

#Resizing
resized = cv.resize(img , (600,600),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#cropping
cropping = img[0:100 , 200:400]
cv.imshow('cropped',cropping)


cv.waitKey(0)


