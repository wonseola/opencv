import cv2
import numpy as np


img = cv2.imread('./res/222.jpg')
rows, cols = img.shape[:2]

w = int(cols/7)
h = int(rows/5)




cv2.imshow('d', img)
cv2.waitKey(0)
cv2.destroyAllWindows()