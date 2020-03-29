import cv2 as cv
import numpy as np

# img = cv.imread("messi5.jpg", cv.IMREAD_GRAYSCALE)
# lap = cv.Laplacian(img, cv.CV_64F)
# lap = np.uint8(np.absolute(lap))
#
# cv.imshow("lap", lap)
# cv.waitKey(0)
# cv.destroyAllWindows()
ddepth = cv.CV_16S
kernel_size = 3
window_name = "Laplace Demo"

img = cv.imread('lena.jpg', 1)

g = cv.GaussianBlur(img, (3, 3), 0)
src_gray = cv.cvtColor(g, cv.COLOR_BGR2GRAY)
lap = cv.Laplacian(src_gray, ddepth, 3)
abs_dst = cv.convertScaleAbs(lap)
cv.imshow('s', abs_dst * 4 + 128)
cv.waitKey(0)
cv.destroyAllWindows()

