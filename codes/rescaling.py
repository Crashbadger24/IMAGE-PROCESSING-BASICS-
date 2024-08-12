import cv2 as cv

def frame_scaler(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)

#Only for live video
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)
    

img = cv.imread(r"D:\python\Learning_ML\Imageprocessing\ImagesandVideos\WhatsApp Image 2024-05-28 at 16.21.05_4d8c4238.jpg")
cv.imshow('IMAGE',img)
cv.imshow('IMAGE2',frame_scaler(img,scale=0.5))

capture = cv.VideoCapture(r"D:\python\Learning_ML\Imageprocessing\ImagesandVideos\WhatsApp Video 2024-05-28 at 16.21.10_b38e5b3b.mp4")

while True:
    ret , frame = capture.read()
    cv.imshow('Video',frame)
    resized_frame = frame_scaler(frame , scale =0.1 )
    cv.imshow('RESIZED VIDEO',resized_frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)