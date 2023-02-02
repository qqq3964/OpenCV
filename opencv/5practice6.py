import cv2
import numpy as np
blue = (255,0,0)
image = cv2.imread('ch05_images/color.jpg',cv2.IMREAD_COLOR)
mask = np.zeros(image.shape[:2],np.uint8)
mask2 = np.zeros(image.shape[:2],np.uint8)
pt1,pt2 = (100,200),(250,300)
pt3,pt4 = (50,100),(100,150)
print(image.shape)
cv2.rectangle(image,pt1,pt2,blue,3,cv2.LINE_4)
cv2.rectangle(image,pt3,pt4,blue,3,cv2.LINE_4)

blue,green,red = cv2.split(image)
mask[200:300,100:250] = 50
mask2[100:50,150:100] = 255
 
a_b,a_g,a_r = cv2.split(a)
blue += mask
green += mask
red += mask
min_val,max_val,_,_ = cv2.minMaxLoc(a_b)
ratio = 255/(max_val-min_val)

image = cv2.merge([blue,green,red])
cv2.imshow('hi',image) 
cv2.waitKey(0)