'''
컬러 영상을 입력받아서, YCbCr 컬러 공간으로 변환하고 다시 환원하는 프로그램을 작성하시오.
'''
import cv2
import numpy as np

image = cv2.imread('ch06_images/color_space.jpg')

YCC_img = cv2.cvtColor(image,cv2.COLOR_BGR2YCrCb)

Y,Cr,Cb = cv2.split(YCC_img)
titles = ['Y','Cr','Cb']
for t in titles:    cv2.imshow(t,eval(t))
cv2.waitKey(0)