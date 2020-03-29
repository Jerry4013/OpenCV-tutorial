import cv2 as cv

# img = cv2.imread('lena.jpg', -1)
# cv2.imshow('image', img)
# k = cv2.waitKey(0)
#
# if k == 27:
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('lena_copy.png', img)
#     cv2.destroyAllWindows()

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while(True):
    ret, frame = cap.read()
    if ret:
        cap.get(cv.CAP_PROP_FRAME_WIDTH)
        cap.get(cv.CAP_PROP_FRAME_HEIGHT)
        out.write(frame)
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()