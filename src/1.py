import cv2
import numpy as np

def line(img, a, b):
    rows, cols = img.shape[:2]
    # print(f"{rows}  , {cols}")
    w, h = int(cols/a) ,int(rows/b)
    # print(f"{w}  , {h}")
    for j in range(a):
        cv2.line(img, (j*w,0),(j*w,rows), (255,255,255))
        for i in range(b):
            cv2.line(img, (cols,h*i),(0,h*i), (255,255,255)) 
            cv2.putText(img,(f"{i} {j}"), [j * w, i * h + 15], cv2.QT_FONT_NORMAL, 0.5, (255,255,255), 1, cv2.LINE_AA)
            x, y= j * w, i * h
            roi = img[y:y+h, x:x+w] 
            m = cv2.mean(roi)
            img_mean = int(m[0]+ m[1]+ m[2])
            # print(f"{img_mean}")
            cv2.putText(img,(f"{img_mean}"), [j * w + 20, i * h + 50], cv2.QT_FONT_NORMAL, 0.5, (128,255,0), 1, cv2.LINE_AA)

img = cv2.imread('./res/222.jpg')
# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# mask = cv2.inRange(img1, (-50,0,100), (130,255,255))
# img1 = cv2.copyTo(img1, mask = mask)
# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

line(img,7,5)

cv2.imshow('d', img)
cv2.waitKey(0)
cv2.destroyAllWindows()