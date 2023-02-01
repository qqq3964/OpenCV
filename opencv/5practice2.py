import cv2
import numpy as np

capture = cv2.VideoCapture(0)
if capture.isOpened() == False: raise Exception('안열림')

fps = 30
delay = round(1000/fps)
mean_val = 0
while True :
    ret,frame = capture.read()
    if not ret: break
    if cv2.waitKey(delay) >= 0: break
    mask = np.zeros(frame.shape[:2],np.uint8)
    mask[100:,200:] = 255
    mean_val = cv2.mean(frame,mask)
    print(mean_val) 
    cv2.imshow('view frame',frame)
capture.release()