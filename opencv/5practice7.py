# 두 개의 트랙바를 추가해서 각 영상의 반영 비율 조절
import numpy as np, cv2

image1 = cv2.imread('ch06_images/add1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('ch06_images/add2.jpg', cv2.IMREAD_GRAYSCALE)

alpha, beta = 0.6, 0.7
image = cv2.addWeighted(image1, alpha, image2, beta, 0)

def onChangeAlpha(value):
    global image, alpha
    alpha = (value / 100)
    image = cv2.addWeighted(image1, alpha, image2, beta, 0)
    cv2.imshow(title, np.hstack([image1, image, image2]))

def onChangeBeta(value):
    global image, beta
    beta = (value / 100)
    image = cv2.addWeighted(image1, alpha, image2, beta, 0)
    cv2.imshow(title, np.hstack([image1, image, image2]))

title = 'dst'
cv2.imshow(title, np.hstack([image1, image, image2]))

cv2.createTrackbar('image1', title, int(alpha*100), 100, onChangeAlpha)
cv2.createTrackbar('image2', title, int(beta*100), 100, onChangeBeta)
cv2.waitKey(0)