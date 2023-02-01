import numpy as np
import cv2

m1 = np.full((3,6),10,np.uint8)             # 단일채널 생성 및 초기화
m2 = np.full((3,6),5,np.uint8) 
m_mask = np.zeros(m1.shape,np.uint8)        # 마스크 생성
m_mask[:,3:] = 1

## 행렬 덧셈 수행
m_add1 = cv2.add(m1,m2)
m_add2 = cv2.add(m1,m2,mask=m_mask)

## 행렬 나눗생 수행
m_div1 = cv2.divide(m1,m2)
m1 = m1.astype(np.float32)                  # 이곳에서 m1을 float 형태로 수정함
m2 = np.float32(m2)
m_div2 = cv2.divide(m1,m2)

titles = ['m1','m2','m_mask','m_add1','m_add2','m_div1','m_div2']
for title in titles:
    print(f'{title} = \n {eval(title)}')