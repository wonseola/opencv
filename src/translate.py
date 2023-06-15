import cv2
import numpy as np

img = cv2.imread('./res/img.jpg')
rows, cols = img.shape[:2]

dx, dy = 100, 50

mtrx = np.float32([
    [1, 0, dx],
    [0, 1, dy]
    ])

dst1 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy))
dst2 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None, cv2.INTER_LINEAR, cv2.BORDER_CONSTANT, (153, 153, 255))
dst3 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None, cv2.INTER_LINEAR, cv2.BORDER_REFLECT)

cv2.imshow("img", img)
cv2.imshow("1", dst1)
cv2.imshow("2", dst2)
cv2.imshow("3", dst3)

cv2.waitKey()
cv2.destroyAllWindows()