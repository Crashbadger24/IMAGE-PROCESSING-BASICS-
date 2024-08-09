import cv2 as cv

#img = cv.imread(r"D:\python\Learning_ML\Imageprocessing\ImagesandVideos\WhatsApp Image 2024-05-28 at 16.21.05_4d8c4238.jpg")

#cv.imshow('IMAGE',img)
capture = cv.VideoCapture(r"D:\python\Learning_ML\Imageprocessing\ImagesandVideos\WhatsApp Video 2024-05-28 at 16.21.10_b38e5b3b.mp4")

while True:
    ret , frame = capture.read()
    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)