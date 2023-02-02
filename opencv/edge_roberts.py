import cv2
import numpy as np
from Common.filters import filter

def differentail(image,data1,data2):
    mask1 = np.array(data1,np.float32).reshape(3,3)
    mask2 = np.array(data2,np.float32).reshape(3,3)

    dst1 = filter(image,mask1)
    dst2 = filter(image,mask2)
    dst1,dst2 = np.abs(dst1),np.abs(dst2)
    dst = cv2.magnitude(dst1,dst2)

    dst = np.clip(dst,0,255).astype('uint8')    # 윈도우 영상 표시위한
    dst1 = np.clip(dst,0,255).astype('uint8')   # 형변환 및 클램핑
    dst2 = np.clip(dst,0,255).astype('uint8')
    return dst,dst1,dst2                        # 3개 결과 행렬 변환

image = cv2.imread('ch07_images/edge.jpg',cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception('오류')

data1 = [-1,0,0,
          0,1,0,
          0,0,0]

data2 = [0,0,-1,
         0,1,0,
         0,0,0]
         
dst,dst1,dst2 = differentail(image,data1,data2)
cv2.imshow('image',image)
cv2.imshow('roberts edge',dst)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.waitKey(0)