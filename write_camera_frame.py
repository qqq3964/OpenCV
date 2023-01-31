import cv2

capture = cv2.VideoCapture(0)
if capture.isOpened() == False: raise Exception('카메라 연결 안됨')

fps = 29.97                 # 초당 프레임 수
delay = round(1000/fps)     # 프레임 간 지연 시간
size = (640,360)
fourcc = cv2.VideoWriter_fourcc(*'DX50')

## 카메라 속성 실행창에 출력
print('width x heigth: ', size)
print(f'VideoWriterfourcc: {fourcc}')
print(f'delay: {delay} ms')
print(f'fps: {fps:.2}')

capture.set(cv2.CAP_PROP_ZOOM,1)
capture.set(cv2.CAP_PROP_FOCUS,0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,size[0])
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,size[1])

## 동영상 파일 개방 및 코덱, 해상도 설정
writer = cv2.VideoWriter('images/video_file.avi',fourcc,fps,size)
if writer.isOpened() == False: raise Exception('동영상 파일 개방 안됨')

while True:
    ret,frame = capture.read()
    if not ret: break
    if cv2.waitKey(delay) >= 0: break

    writer.write(frame)
    cv2.imshow('View Frame from Camera',frame)

writer.release()
capture.release()