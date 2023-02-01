import numpy as np,cv2

image = cv2.imread('ch05_images/minMax.jpg',cv2.IMREAD_GRAYSCALE)
if image is None:raise Exception('영상파일 읽기 오류 발생')


min_val,max_val,_,_ = cv2.minMaxLoc(image)      # 최소값과 최대값 가져오기
ratio = 255/(max_val-min_val)
dst = np.round((image-min_val)*ratio).astype('uint8')
min_dst,max_dst,_,_ = cv2.minMaxLoc(dst)

print(f'원본 영상 최소값 = {min_val} 최대값 = {max_val}')
print(f'원본 영상 최소값 = {min_dst} 최대값 = {max_dst}')
cv2.imshow('image',image)
cv2.imshow('dst',dst)
cv2.waitKey(0)