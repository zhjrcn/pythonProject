import cv2 as cv
image = cv.imread(r"C:\Users\zhjr\Desktop\22.jpg")
hist = cv.calcHist([image],[2],None,[256],[0,255])
print(hist)

import matplotlib.pyplot as plt
plt.plot(hist)
plt.plot(hist,'r')
#plt.show()

image=image.ravel()
plt.hist(image,256)
cv.waitKey()
cv.destroyAllWindows()
#plt.show()

import numpy as np
image = cv.imread(r"C:\Users\zhjr\Desktop\22.jpg")
imageMax=np.max(image)
imageMin=np.min(image)
min1=0
max1=255
m=float(max1-min1)/(imageMax-imageMin)
n=min1-min1*m
image1 =m*image+n
image1=image1.astype(np.uint8)
#cv.imshow("image",image)
#plt.figure("original hist")
#plt.hist(image.ravel(),256)

#cv.imshow("image1",image1)
#plt.show()
#cv.waitKey()
#cv.destroyAllWindows()


