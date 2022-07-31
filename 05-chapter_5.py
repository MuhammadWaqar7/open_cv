import cv2 as cv
from cv2 import imshow
from cv2 import imwrite
img=cv.imread("resources/image1.jpg") 
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
(thresh,binary)=cv.threshold(gray,127,255,cv.THRESH_BINARY)
img =cv.resize(img,(800,600))
imwrite('resources/image1.png',gray)
imwrite('resources/image1.png',binary)
imshow('gray',gray)
imshow('Black and White',BINARY)
cv.waitKey(0)
cv.destroyAllWindows()