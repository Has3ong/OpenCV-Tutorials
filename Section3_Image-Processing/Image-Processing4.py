import cv2
import os
import numpy as np

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))

image = cv2.imread(__BASE_DIR__ + '/src/car.png').astype(np.float32) / 255
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

kernel = np.ones(shape=(5, 5), dtype=np.float32) / 25

dst = cv2.filter2D(image, -1, kernel)
blurred = cv2.blur(image, ksize=(5, 5))
gauss_blur = cv2.GaussianBlur(image, (5, 5), 10)
median = cv2.medianBlur(image, 5)

#cv2.imshow('Image', image)
#cv2.imshow('dst', dst)
#cv2.imshow('blurred', blurred)
#cv2.imshow('Gaus', gauss_blur)
cv2.imshow('Median', median)
cv2.waitKey()