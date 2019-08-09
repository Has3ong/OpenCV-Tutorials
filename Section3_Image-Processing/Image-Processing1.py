import cv2
import matplotlib.pyplot as plt
import os

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))

image = cv2.imread(__BASE_DIR__ +'/src/bird.jpg')
cv2.imshow('Bird', image)
cv2.waitKey()

image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
cv2.imshow('Bird', image)
cv2.waitKey()

image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('Bird', image)
cv2.waitKey()