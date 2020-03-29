import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('messi5.jpg', 0)
canny = cv.Canny(img, 100, 200)
# cv.imshow('canny', canny)
# cv.waitKey(0)
# cv.destroyAllWindows()

# title = ['image']
# image = [img]
# for i in range(1):
#     plt.subplot(1, 1, i + 1), plt.imshow(image[i], 'gray')
#     plt.title(title[i])
#     plt.xticks([]), plt.yticks([])
#
# plt.show()

im = np.zeros((128, 128))
im[32:-32, 32:-32] = 1
cv.imshow('canny', im)
cv.waitKey(0)
cv.destroyAllWindows()
