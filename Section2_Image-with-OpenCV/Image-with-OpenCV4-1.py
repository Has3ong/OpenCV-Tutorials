import cv2
import numpy as np

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x, y), 100, (0, 255, 128), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(image, (x, y), (x+100, y+100), (128, 188, 57), -1)


winname = 'OpenCV2'
cv2.namedWindow(winname=winname)
cv2.setMouseCallback(winname, draw_circle)


image = np.zeros((512, 512, 3), np.int8)

while True:
    cv2.imshow(winname, image)
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destoryAllWindows()
