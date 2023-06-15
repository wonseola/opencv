import cv2
import pafy

# url = "https://www.youtube.com/watch?v=nY--BputWp0"
url = "https://www.youtube.com/watch?v=QyBdhdz7XM4"

# url 영상 다운
videoInfo = pafy.new(url)
print(videoInfo)
best = videoInfo.getbest(preftype='mp4')

# 캡쳐 구성ㅇ
videoPath = best.url
cap = cv2.VideoCapture(videoPath)

if cap.isOpened():

    # 녹화 정의
    saveFile = './recode.avi'
    fps = 30.0
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
        # 표시
        cv2.imshow('video', frame)
                
        # 저장
        out.write(frame)

        if cv2.waitKey(int(1000/fps)) >= 0:
            break
    out.release()
    pass

cap.release()
cv2.destroyAllWindows()

