import cv2
import numpy as np

def draw_histo(hist,shape=(200,256)):
    hist_img = np.full(shape,255,np.uint8)
    cv2.normalize(hist,hist,0,shape[0],cv2.NORM_MINMAX)
    gap = hist_img.shape[1]/hist.shape[0]

    for i,h in enumerate(hist):
        x = int(round(i*gap))
        w = int(round(gap))
        cv2.rectangle(hist_img,(x,0,w,int(h)),0,cv2.FILLED)
    return cv2.flip(hist_img,0)

image = cv2.imread('ch06_images/pixel.jpg',cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception('안됨')

hist = cv2.calcHist([image],[0],None,[32],[0,256])
hist_img = draw_histo(hist)

cv2.imshow('image',image)
cv2.imshow('hist_img',hist_img)
cv2.waitKey(0)