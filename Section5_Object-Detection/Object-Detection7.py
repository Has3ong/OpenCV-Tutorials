import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))
coins = cv2.imread(__BASE_DIR__+'/src/pennies.jpg')

plt.imshow(coins)
plt.show()

step1 = cv2.medianBlur(coins, 25)
step1 = cv2.cvtColor(step1, cv2.COLOR_BGR2GRAY)

ret, step1 = cv2.threshold(step1, 160, 255, cv2.THRESH_BINARY_INV)
image, contours, hierarchy = cv2.findContours(step1.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(coins, contours, i, (255, 0, 0), 20)

plt.imshow(step1)
plt.show()
plt.imshow(coins, cmap='gray')
plt.show()

step2 = cv2.medianBlur(coins, 35)

step2 = cv2.cvtColor(step2, cv2.COLOR_BGR2GRAY)

ret, step2 = cv2.threshold(step2, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(step2, cv2.MORPH_OPEN, kernel, iterations=2)

step2_baground = cv2.dilate(opening, kernel, iterations=3)

dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, step2 = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

step2 = np.uint8(step2)
unknown = cv2.subtract(step2_baground, step2)

ret, markers = cv2.connectedComponents(step2)
markers = markers+1
markers[unknown==255] = 0

markers = cv2.watershed(coins, markers)
plt.imshow(markers)
plt.show()

image, contours, hierarchy = cv2.findContours(markers.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):

    if hierarchy[0][i][3] == -1:
        cv2.drawContours(coins, contours, i, (255, 0, 0), 10)

plt.imshow(coins)
plt.show()