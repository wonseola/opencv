import cv2
import numpy as np

img = cv2.imread('./res/img.jpg')
height, width = img.shape[:2]

sss=0.5
bbb=2

m_small = np.float32([
    [sss, 0, 0],
    [0, sss, 0]
    ])  
m_big = np.float32([
    [bbb, 0, 0],
    [0, bbb, 0]
    ])  

size_s = (int(width*sss), int(height*sss))
size_b = (int(width*bbb), int(height*bbb))

dst1 = cv2.warpAffine(img, m_small, size_s)
dst2 = cv2.warpAffine(img, m_big, size_b)
dst3 = cv2.warpAffine(img, m_small, size_s, None, cv2.INTER_AREA)
dst4 = cv2.warpAffine(img, m_big, size_b, None, cv2.INTER_CUBIC)

cv2.imshow("img", img)
# cv2.imshow("1", dst1)
# cv2.imshow("2", dst2)
cv2.imshow("1-1", dst3)
cv2.imshow("2-1", dst4)

cv2.waitKey(0)
cv2.destroyAllWindows()