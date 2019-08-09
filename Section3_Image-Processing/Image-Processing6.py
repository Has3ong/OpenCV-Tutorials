import cv2
import os
import numpy as np

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))
image = cv2.imread(__BASE_DIR__ + '/src/valve.png', cv2.IMREAD_GRAYSCALE)

sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

laplacian = cv2.Laplacian(image, cv2.CV_64F)
blend = cv2.addWeighted(src1=sobelx, alpha=0.5, src2=sobely, beta=0.5, gamma=0)

#cv2.imshow('Image', image)
#cv2.imshow('Sobel', sobelx)
#cv2.imshow('SobelY', sobely)
#cv2.imshow('Laplacian', laplacian)
#cv2.imshow('Blend', blend)

cv2.waitKey()