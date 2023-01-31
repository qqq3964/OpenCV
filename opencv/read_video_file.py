import cv2
from Common.utils import put_string

capture = cv2.VideoCapture(0)
if not capture.isOpened(): raise Exception('동영상 팡리 개방 안됨')

frame_rate = capture.get(cv2.CAP_PROP_FPS)          # 초당 프레임 수
delay = int(1000/frame_rate)                        # 지연 시간
frame_cnt = 0                                       # 현재 프레임번호

while True:
    ret,frame = capture.read()
    if not ret or cv2.waitKey(delay) >= 0: break    # 프레임 간 지연 시간 지정
    blue,green,red = cv2.split(frame)               # 컬러 영상 채널 분리
    frame_cnt += 1

    if 100 <= frame_cnt < 200: cv2.add(blue,100,blue)
    elif 200 <= frame_cnt < 300: cv2.add(green,100,green)
    elif 300 <= frame_cnt <400: cv2.add(red,100,red)

    frame = cv2.merge([blue,green,red])
    put_string(frame,'frame_cnt: ',(20,30),frame_cnt)
    cv2.imshow('Read Video File',frame)
capture.release()