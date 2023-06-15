import cv2
import pafy
# from cap_from_youtube import cap_from_youtube

url = "https://www.youtube.com/watch?v=nY--BputWp0"
# url = "https://www.youtube.com/watch?v=QyBdhdz7XM4"

video = pafy.new(url)
best = video.getbest()

cap = cv2.VideoCapture(best.url)

if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow(best.url, frame)
        if cv2.waitKey(25) >=0:
            break
        pass
    pass
else:
    print("no frame")

cap.release()
cv2.destroyAllWindows()

