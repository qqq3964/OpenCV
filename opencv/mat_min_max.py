import numpy as np,cv2

data = [10,200,5,7,9,
        15,35,60,80,170,
        100,2,55,37,70]
m1 = np.reshape(data,(3,5))
m2 = np.full((3,5),50)

m_min = cv2.min(m1,30)
m_max = cv2.min(m1,m2)

## 행렬의 최솟값/최댓값과 그 좌표들을 반환
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(m1)

print(f'[m1] = \n{m1}')
print(f'[m_min] = \n{m_min}')
print(f'[m_max] = \n{m_max}')

## min_loc와 max_loc 좌표는(y,x)이므로 행렬의 좌표 위치와 반대임
print(f'm1 행렬 최소값 좌표{min_loc} 최소값: {min_val}')
print(f'm1 행렬 최소값 좌표{max_loc} 최소값: {max_val}')

