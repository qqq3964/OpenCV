import numpy as np
import cv2

blue,green = (255,0,0),(0,255,0)
white = (255,255,255)
line = 1
size = 0
def onMouse(event,x,y,flags,param):
    global title,line,size
    pt1 = (x,y)
    pt2 = (x+30+size,y+30+size)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image,pt1,20+size,blue,line)
        cv2.imshow(title,image)
    elif event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image,pt1,pt2,green,thickness=size+1)
        cv2.imshow(title,image)

def onChange(value):
    global image,bar_name,line,size

    line = value
    size = value
    cv2.setTrackbarPos(bar_name,title,value)
    cv2.imshow(title,image)
    

image = np.full((300,400,3),white,np.uint8)
title = 'Trackbar & Mouse Event'
bar_name = 'Trackbar'
cv2.imshow(title,image)

cv2.createTrackbar('Trackbar',title,0,50,onChange)
cv2.setMouseCallback(title,onMouse)
cv2.waitKey(0)