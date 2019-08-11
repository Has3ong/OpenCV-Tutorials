import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))

image = cv2.imread(__BASE_DIR__ + '/src/board.png', cv2.COLOR_BGR2RGB)

plt.imshow(image)
plt.show()

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray_image)

dst = cv2.cornerHarris(src=gray,blockSize=5,ksize=3,k=0.04)

dst = cv2.dilate(dst,None)

image[dst>0.01*dst.max()]=[255,0,0]

plt.imshow(image)
plt.show()