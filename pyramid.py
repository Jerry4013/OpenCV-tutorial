import cv2 as cv


img = cv.imread("lena.jpg")
# lr1 = cv.pyrDown(img)
# lr2 = cv.pyrDown(lr1)
# hr2 = cv.pyrUp(lr2)

# cv.imshow("Original image", img)
# cv.imshow("pyrDown1 image", lr1)
# cv.imshow("pyrDown1 image", lr2)
# cv.imshow("pyrUp 1 image", hr2)
# cv.waitKey(0)
# cv.destroyAllWindows()

layer = img.copy()
gp = [layer]
lp = []
for i in range(3):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    lap = cv.subtract(gp[i], cv.pyrUp(layer))
    lp.append(lap)
# cv.imshow("final", down)
# cv.imshow("original", layer)
# lap = cv.subtract(layer, down)
# cv.imshow("lap", lap)

for i in range(2, 0, -1):
    layer = cv.add(cv.pyrUp(layer), lp[i])
cv.imshow("recover", layer)
cv.imshow("origin", cv.pyrDown(img))
cv.waitKey(0)
cv.destroyAllWindows()


