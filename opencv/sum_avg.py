import numpy as np,cv2

image = cv2.imread('ch05_images/sum_test.jpg',cv2.IMREAD_COLOR)
if image is None:raise Exception('오류입니다.')

mask = np.zeros(image.shape[:2],np.uint8)
mask[60:160,20:120] = 255               # 관심 영역에 255 할당

sum_value = cv2.sumElems(image)         # 채널별 합 - 튜플로 반환
mean_value1 = cv2.mean(image)           # 채널 평균 - 튜플로 반환
mean_value2 = cv2.mean(image,mask)

print(f'sum_value 자료형 {type(sum_value)} {type(sum_value[0])}')
print(f'[sum_value] = {sum_value}')
print(f'[mena_value1] = {mean_value1}')
print(f'[mena_value2] = {mean_value2}')
print()

## 평균과 표준편차 결과 저장
mean, stddev = cv2.meanStdDev(image)
mean2,stddev2 = cv2.meanStdDev(image,mask=mask)
print('mean 자료형',type(mean),type(mean[0][0]))
print(f'[mean] = {mean.flatten()}')
print(f'[stddev] = {stddev.flatten()}')
print()

print(f'[mean2] = {mean2.flatten()}')
print(f'[stddev2] = {stddev2.flatten()}')

cv2.imshow('image',image)
cv2.imshow('mask',mask)
cv2.waitKey(0)