import cv2 as cv
import time 

video =cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier("D:\python\Learning_ML\Imageprocessing\haar_face.xml")
max_duration=10

start_time = time.time()
while True:
    ret,frame= video.read()
    if ret:
        faces_count = haar_cascade.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=3)
        for (x,y,w,h) in faces_count:
         cv.rectangle(frame,(x,y),(x+h,y+h),(0,255,0),thickness=1)
        cv.imshow('faces',frame)
    current_time = time.time()
    if current_time - start_time > max_duration:
        break
    cv.waitKey(30)
    
cv.destroyAllWindows()
video.release()