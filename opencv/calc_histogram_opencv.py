import numpy as np,cv2

def calc_histo(image,hsize,ranges=[0,256]):
    hist = np.zeros((hsize,1),np.float32)
    gap = ranges[1]/hsize
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            idx = int(image.item(i,j)/gap)
            hist[idx] += 1
    return hist

image = cv2.imread('ch06_images/pixel.jpg',cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception('영상 파일 읽기 오류 발생')

histSize,ranges = [32],[0,256]
gap = ranges[1]/histSize[0]
ranges_gap = np.arange(0,ranges[1]+1,gap)
hist1 = calc_histo(image,histSize[0],ranges)
hist2 = cv2.calcHist([image],[0],None,histSize,ranges)
hist3,bins = np.histogram(image,ranges_gap)

print('user 함수\n', hist1.flatten())
print('opencv 함수\n', hist2.flatten())
print('numpy 함수\n', hist3)