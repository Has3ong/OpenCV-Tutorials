import cv2
import numpy as np

drawing = False
dx, dy = -1, -1

def draw_circle(event, x, y, flags, param):
    global drawing, dx, dy
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        dx, dy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(image, (dx, dy), (x, y), (255, 0, 0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

winname = 'OpenCV2'
cv2.namedWindow(winname=winname)
cv2.setMouseCallback(winname, draw_circle)

image = np.zeros((512, 512, 3), np.int8)

while True:
    cv2.imshow(winname, image)
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destoryAllWindows()
