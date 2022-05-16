import cv2 as cv
import numpy as np
image = cv.imread("C:/Users/zhjr/Desktop/22.jpg")
faceCascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, scaleFactor=1.03, minNeighbors=3, minSize=(3, 3))
print(faces)
print("发现{0}个人脸".format(len(faces)))
for (x, y, w, h) in faces:
    cv.circle(image, (int((x+x+w)/2),int((y+y+h)/2)), int(w/2), (0, 255, 0), 2)
cv.imshow("dect", image)
cv.waitKey()
cv.destroyAllWindows()