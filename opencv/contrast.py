import numpy as np
import cv2

image = cv2.imread('ch06_images/contrast.jpg',cv2.IMREAD_GRAYSCALE) # 영상읽기
if image is None: raise Exception('영상 파일 읽기 오류')

noimage = np.zeros(image.shape[:2],image.dtype)
avg = cv2.mean(image)[0]/2.0

dst1 = cv2.scaleAdd(image,0.5,noimage)              # 명암 대비 감소
dst2 = cv2.scaleAdd(image,2.0,noimage)              # 명암 대비 증가
dst3 = cv2.addWeighted(image,0.5,noimage,0,avg)     # 명암 대비 감소
dst4 = cv2.addWeighted(image,2.0,noimage,0,-avg)    # 명암 대비 증가

cv2.imshow('image',image)
cv2.imshow('dst1-decrease contrast',dst1)
cv2.imshow('dst1-increase contrast',dst2)
cv2.imshow('dst1-decrease contrast using average',dst3)
cv2.imshow('dst4-increase contrast using average',dst4)
cv2.waitKey(0)