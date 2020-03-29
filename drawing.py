import numpy as np
import cv2 as cv

# img = cv.imread('lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)

img = cv.line(img, (0, 0), (255, 255), (0, 0, 255), 5)
img = cv.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 10)

img = cv.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 5)  # 最后一个参数用-1表示填充整个图形
img = cv.circle(img, (447, 63), 63, (0, 255, 0), -1)
font = cv.FONT_HERSHEY_COMPLEX
img = cv.putText(img, 'OpenCV', (10, 500), font, 4, (0, 255, 255), 10, cv.LINE_AA)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()

