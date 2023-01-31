import numpy as np
import cv2

B,G,R = (255,0,0),(0,255,0),(0,0,255)
image = np.zeros((400,600,3),np.uint8)
image[:] = (255,255,255)

pt1,pt2 = (50,50),(250,150)
pt3,pt4 = (400,150),(500,50)
roi = (50,200,200,100)                              # 사각형 영역 4원소 튜플

## 직선 그리기
cv2.line(image,pt1,pt2,R)
cv2.line(image,pt3,pt4,G,cv2.LINE_AA)               # 계단현상 감소

## 사각형 그리기
cv2.rectangle(image,pt1,pt2,B,3,cv2.LINE_4)         # 4방향 연결선
cv2.rectangle(image,roi,R,3,cv2.LINE_8)             # 8방향 연결선
cv2.rectangle(image,(400,200,100,100),G,cv2.FILLED) # 내부 채움

cv2.imshow("Line & Rectangle",image)
cv2.waitKey(0)
cv2.destroyAllWindows()