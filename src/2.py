import cv2
import numpy as np

img = cv2.imread('./res/1.jpg')
rows, cols = img.shape[0:2]
print(f"{rows}  , {cols}")

w = int(cols/7)
h = int(rows/5)
for j in range(7):
    cv2.line(img, (j*w,0),(j*w,rows), (255,255,255))
    for i in range(5):
        cv2.line(img, (cols,h*i),(0,h*i), (255,255,255)) 
        cv2.putText(img,(f'{i},{j}'), [j * w, i * h], cv2.QT_FONT_NORMAL, 0.5, (255,255,255), 1, cv2.LINE_AA)
        #???????????????????아

cv2.imshow('d', img)
cv2.waitKey(0)
cv2.destroyAllWindows()