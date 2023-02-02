import numpy as np
import cv2

## 컨볼루션 수행 함수 - 행렬 처리 방식
def filter(image,mask):
    rows,cols = image.shape[:2]
    dst = np.zeros((rows,cols),np.float32)
    xcenter,ycenter = mask.shape[1]//2,mask.shape[0]//2

    for i in range(ycenter,rows-ycenter):
        for j in range(xcenter,cols-xcenter):
            y1,y2 = i - ycenter,i+ycenter+1 # 관심 영역 높이 범위
            x1,x2 = j - xcenter,j+xcenter+1 # 관심 영역 너비 범위
            roi = image[y1:y2,x1:x2].astype('float32')
            tmp = cv2.multiply(roi,mask)
            dst[i,j] = cv2.sumElems(tmp)[0]
    return dst

image = cv2.imread('ch07_images/filter_blur.jpg',cv2.IMREAD_GRAYSCALE)

data = [[1/9,1/9,1/9],
        [1/9,1/9,1/9],
        [1/9,1/9,1/9]]

mask = np.array(data,np.float32).reshape(3,3)
blur1 = filter(image,mask)
blur1 = blur1.astype('uint8')

cv2.imshow('image',image)
cv2.imshow('blur1',blur1)
cv2.waitKey(0)