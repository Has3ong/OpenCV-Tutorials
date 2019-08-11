import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))
image = cv2.imread(__BASE_DIR__ + '/src/board.png')

plt.imshow(image)
plt.show()

found, corners = cv2.findChessboardCorners(image, (7, 7))

image_copy = image.copy()
cv2.drawChessboardCorners(image_copy, (7, 7), corners, found)
plt.imshow(image_copy)
plt.show()
