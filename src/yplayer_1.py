import cv2
import pafy
import numpy as np

def color (origin:cv2.Mat, c) -> cv2.Mat:
        frame = origin.copy()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower = np.array([(c-20), 30, 30])
        upper = np.array([(c+20), 300, 300])
        mask = cv2.inRange(hsv, lower, upper)
        a = cv2.bitwise_and(frame, frame, mask=mask)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray1 = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        mask1 = cv2.bitwise_not(mask)
        b = cv2.bitwise_and(gray1, gray1, mask=mask1)

        res = cv2.bitwise_or(a, b)
        return res

url = 'https://www.youtube.com/watch?v=mXtpjBzPMeY'

# url 영상 다운
videoInfo = pafy.new(url)
print(videoInfo)
best = videoInfo.getbest(preftype='mp4')

# 캡쳐 구성ㅇ
videoPath = best.url
cap = cv2.VideoCapture(videoPath)

if cap.isOpened():

    # 녹화 정의
    saveFile = './cartoon.avi'
    fps = 60.0
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    # 영상크기
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = int(width), int(height)
    # 어떻게 저장할지>??>?????/
    out = cv2.VideoWriter(saveFile, fourcc, fps, size)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # cartoon_image1 = cv2.stylization(frame, sigma_s=20, sigma_r=0.23)

        res = color(frame,1,1)
        cv2.imshow('video2', res)

        # 저장
        # out.write()

        if cv2.waitKey(int(1000/fps)) >= 0:
            break
    out.release()
    pass

cap.release()
cv2.destroyAllWindows()




