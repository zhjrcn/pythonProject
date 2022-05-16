import cv2 as cv
image = cv.imread(r"C:\Users\zhjr\Desktop\22.jpg")
cv.imshow("image", image)
gauss = cv.GaussianBlur(image,(5,5),0,0)
bi=cv.bilateralFilter(image,5,10,10)
cv.imshow("gauss",gauss)
cv.imshow("bi", bi)
cv.waitKey()
cv.destroyAllWindows()