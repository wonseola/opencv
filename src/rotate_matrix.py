import cv2
import numpy as np

img = cv2.imread('./res/img.jpg')
rows, cols = img.shape[:2]

d45 = 45.0 * np.pi /180
d90 = 90.0 * np.pi /180

# m45 = np.float32( [
#     [ np.cos(d45), -1* np.sin(d45), rows//2],
#     [np.sin(d45), np.cos(d45), -1*cols//4]
#     ])
# m90 = np.float32( [
#     [ np.cos(d90), -1* np.sin(d90), rows],
#     [np.sin(d90), np.cos(d90), 0]
#     ])

m45 = cv2.getRotationMatrix2D((cols/2,rows/2), 45, 1) 
m90 = cv2.getRotationMatrix2D((cols/2,rows/2), 90, 1) 


r45 = cv2.warpAffine(img,m45,(cols,rows))
r90 = cv2.warpAffine(img,m90,(cols,rows))

cv2.imshow("img", img)
cv2.imshow("45", r45)
cv2.imshow("90", r90)
cv2.waitKey()
cv2.destroyAllWindows()