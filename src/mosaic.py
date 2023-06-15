import cv2
import numpy as np

img = cv2.imread('./res/img.jpg')
rate = 15
while True:
    x,y,w,h = cv2.selectROI('a', img, False)
    roi = img[y:y+h, x:x+w]

    # # 리사이즈
    # roi = cv2.resize(roi, (w//rate, h//rate))
    # roi = cv2.resize(roi, (w,h), interpolation=cv2.INTER_AREA)

    ##평균
    # roi = cv2.mean(roi)
    
    # 블러
    roi = cv2.blur(roi, (30,30))


    img[y:y+h, x:x+w] = roi   # 원본 이미지에 적용
    cv2.imshow('a', img)
cv2.destroyAllWindows()