'''
캐니 에지 알고리즘에서 이중 임계값을 트랙바로 만들어서 두개의
임계값을 조절하여 에지를 검출하도록 프로그램을 작성하시오
'''
import cv2
import numpy as np

def onChange(value):
    global image,title
    threshold1 = cv2.getTrackbarPos('th1',title)
    threshold2 = cv2.getTrackbarPos('th2',title)
    edge_image = cv2.Canny(image, threshold1, threshold2)
    cv2.imshow(title,edge_image)

image = cv2.imread('ch07_images/cannay_tset.jpg',cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception('오류')

title = 'canny image'
cv2.imshow(title,image)

cv2.createTrackbar('th1',title,0,255,onChange)
cv2.createTrackbar('th2',title,0,255,onChange)
cv2.waitKey(0)