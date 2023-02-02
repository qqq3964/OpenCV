import cv2
import numpy as np

'''
가우시안 블러링 평균 필터링을 수행한다.
샤프닝은 3*3 크기의 마스크를 적용한다.
컬러 영상의 채널을 분리해서 각 채널에 블러링과 샤프닝을 수행하고, 다시 합쳐본다
컬러 영상에서 바로 OpenCV 함수인 cv2.filter2D()를 적용해 보자
'''
image = cv2.imread('ch07_images/filter_sharpen.jpg')
if image is None: raise Exception('안되용')

## blur
kernel = np.ones((3,3),dtype=np.float64)/9.
## sharpen
kernel2 = np.ones((3,3),dtype=np.int32)*(-1)
kernel2[1,1] = 9
blue,green,red = cv2.split(image)

## blur
dst_blue = cv2.filter2D(blue,-1,kernel)



dst_green = cv2.filter2D(green,-1,kernel)
dst_red = cv2.filter2D(red,-1,kernel)

## sharpen
dst_blue1 = cv2.filter2D(blue,-1,kernel2)
dst_green1 = cv2.filter2D(green,-1,kernel2)
dst_red1 = cv2.filter2D(red,-1,kernel2)

image1 = cv2.merge([dst_blue,dst_green,dst_red])
image2 = cv2.merge([dst_blue1,dst_green1,dst_red1])

cv2.imshow('image',image)
cv2.imshow('blur',image1)
cv2.imshow('sharpen',image2)
cv2.waitKey(0)