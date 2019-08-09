import cv2
import os
import numpy as np

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))

image = np.zeros((600, 600))
font = cv2.FONT_HERSHEY_SIMPLEX
image = cv2.putText(image, text='ABCDE', org=(50, 300), fontFace=font, fontScale=5, color=(255,255,255), thickness=30)

kernel = np.ones((5, 5), dtype=np.uint8)
erode = cv2.erode(image, kernel, iterations=3)

white_noise = np.random.randint(low = 0, high=2, size=(600,600))
white_noise = white_noise * 255

noise = white_noise + image
morphology = cv2.morphologyEx(noise, cv2.MORPH_OPEN, kernel)

gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

#cv2.imshow('Image', image)
#cv2.imshow('Erode', erode)
#cv2.imshow('Noise', noise)
#cv2.imshow('Morpho', morphology)
cv2.imshow('Gradient', gradient)
cv2.waitKey(0)


