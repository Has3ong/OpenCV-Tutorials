import cv2
import os

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))

image = cv2.imread(__BASE_DIR__ + '/src/house.jpg', cv2.IMREAD_GRAYSCALE)
ret, thresh = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)

cv2.imshow('Source', image)
cv2.imshow('Thresholding', thresh)
cv2.waitKey()
