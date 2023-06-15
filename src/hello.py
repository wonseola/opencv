import cv2

imgPath = './res/1.png'
imgMat = cv2.imread(imgPath)

print(imgMat)

if imgMat is not None:
    cv2.imshow('MAT', imgMat)
    cv2.waitKey()
    cv2.destroyAllWindows()
