# we have to convert in to in black and white
# from importlib import resources

# from gettext import install
# import telnetlib
import cv2 as cv
# import pip
# pip install telnetlib
# from sklearn.feature_extraction import img_to_graph   
img=cv.imread("resources/image1.jpg") 
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
(thresh,binary)=cv.threshold(gray,127,255,cv.THRESH_BINARY)
cv.imshow('original',img)
cv.imshow('gray',gray)
cv.imshow('Black and White',BINARY)
cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv
# import pip
# pip install telnetlib
# from sklearn.feature_extraction import img_to_graph   
img=cv.imread("resources/image1.jpg") 
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
(thresh,binary)=cv.threshold(gray,127,255,cv.THRESH_BINARY)
cv.imshow('original',img)
cv.imshow('gray',gray)
cv.imshow('Black and White',BINARY)
cv.waitKey(0)
cv.destroyAllWindows()