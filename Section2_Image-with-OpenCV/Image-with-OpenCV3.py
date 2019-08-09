import cv2
import numpy as np

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)
yellow = (0, 255, 255)
cyan = (255, 255, 0)
magenta = (255, 0, 255)

width, height = 600, 600
thickness = 2

image = np.zeros((height, width, 3), np.uint8)
pts = np.array(([315, 50], [570, 240], [475, 550], [150, 550], [50, 240]), np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.fillPoly(image, [pts], yellow)

cv2.line(image, pt1=(0, 0), pt2=(600, 600), color=magenta, thickness=thickness)

cv2.rectangle(image, (20, 20), (120, 120), white, 4)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, text='Hello OpenCV', org=(100, 300), fontFace=font, fontScale=2, color=cyan, thickness=thickness, lineType=cv2.LINE_AA)
cv2.imshow("drawing", image)
cv2.waitKey(0);