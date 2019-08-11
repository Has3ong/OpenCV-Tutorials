import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))
image = cv2.imread(__BASE_DIR__ + '/src/smile.png', cv2.COLOR_BGR2RGB)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image, contours, hierarchy = cv2.findContours(image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

external_contours = np.zeros(image.shape)

for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(external_contours, contours, i, 255, -1)

internal_image = np.zeros(image.shape)

for i in range(len(contours)):
    if hierarchy[0][i][3] != -1:
        cv2.drawContours(internal_image, contours, i, 255, -1)

plt.imshow(image, cmap='gray')
plt.show()
plt.imshow(external_contours, cmap='gray')
plt.show()
plt.imshow(internal_image, cmap='gray')
plt.show()