import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))
image = cv2.imread(__BASE_DIR__ + '/src/macbook.jpg', cv2.COLOR_BGR2RGB)

mask = np.zeros(image.shape[:2], np.uint8)
mask[200:800, 100:400] = 255
plt.imshow(mask)
plt.show()

masked = cv2.bitwise_and(image, image, mask=mask)
plt.imshow(masked)
plt.show()