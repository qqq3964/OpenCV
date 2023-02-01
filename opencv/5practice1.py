import numpy as np 
import cv2

image = cv2.imread('ch05_images/color.jpg',cv2.IMREAD_COLOR)        # 영상 읽기
if image is None: raise Exception('영상 파일 읽기 오류')
print(image.shape)
blue = (255,0,0)
center = (190,170)
size = (120,60)

mask = np.zeros(image.shape[:2],np.uint8)
cv2.ellipse(mask,center,size,90,0,360,blue,-1)
dst = cv2.bitwise_and(image,image,mask = mask)

cv2.imshow('h',dst)
cv2.waitKey(0)