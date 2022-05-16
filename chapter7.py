import cv2 as cv
import numpy as np
image = cv.imread(r"C:\Users\zhjr\Desktop\22.jpg", 0)
#gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, dst = cv.threshold(image,127,255,cv.THRESH_BINARY)
admean = cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,5,3)
adguass =cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,5,3)
cv.imshow("image",image)           #原始图像
cv.imshow("dst", dst)              #全局阈值处理，二值化
cv.imshow("admean",admean)         #局部阈值处理，领域权重相同
cv.imshow("adguass",adguass)       #局部阈值处理，高斯方程方式
cv.waitKey()
cv.destroyAllWindows()

t1, thd =cv.threshold(image, 150, 255, cv.THRESH_BINARY)
t2, ostu = cv.threshold(image,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow("image", image)
cv.imshow("thd", thd)
cv.imshow("ostu", ostu)
print("二值化阈值处理的阈值是：%s" % t1)
print("Ostu阈值处理的阈值是： %s" % t2)
cv.waitKey()
cv.destroyAllWindows()