import numpy as np
import cv2

image1 = np.zeros((300,300),np.uint8)
image2 = image1.copy()

h,w = image1.shape[:2]
cx,cy = w//2,h//2
cv2.circle(image1,(cx,cy),100,255,-1)
cv2.rectangle(image2,(0,0,cx,h),255,-1)

image3 = cv2.bitwise_or(image1,image2)              # 원소 간 논리합
image4 = cv2.bitwise_and(image1,image2)             # 원소 간 논리곱
image5 = cv2.bitwise_xor(image1,image2)             # 원소 간 배타적 논리합
image6 = cv2.bitwise_not(image1)                    # 행렬 반전

cv2.imshow('image1',image1);            cv2.imshow('image2',image2)
cv2.imshow('image3',image3);            cv2.imshow('image4',image4)
cv2.imshow('image5',image5);            cv2.imshow('image6',image6)
cv2.waitKey(0)