import cv2 as cv
import numpy as np
image = cv.imread(r"C:\Users\zhjr\Desktop\22.jpg")
#形态梯度学运算：膨胀图像减去腐蚀图像
k1 = np.ones((2, 2), np.uint8)
k2 = np.ones((5, 5), np.uint8)
r1=cv.morphologyEx(image, cv.MORPH_GRADIENT,k1)
r2=cv.morphologyEx(image, cv.MORPH_GRADIENT,k2)
cv.imshow("image",image)
cv.imshow("r1",r1)
cv.imshow("r2",r2)
cv.waitKey()
cv.destroyAllWindows()
#开运算：先膨胀后腐蚀；闭运算，先膨胀后腐蚀
k = np.ones((10,10), np.uint8)
openimg = cv.morphologyEx(image,cv.MORPH_OPEN, k)
cv.imshow("openimg", openimg)
cv.waitKey()
cv.destroyAllWindows()

