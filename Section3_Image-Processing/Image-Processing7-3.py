import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))
image = cv2.imread(__BASE_DIR__ + '/src/macbook.jpg', 0)

hist_values = cv2.calcHist([image], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(hist_values)
plt.show()

eq_macbook = cv2.equalizeHist(image)
#cv2.imshow('equalizeHist', eq_macbook)
#cv2.waitKey()

hist_values = cv2.calcHist([eq_macbook], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(hist_values)
plt.show()