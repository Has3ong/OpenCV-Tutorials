import cv2
import os
import matplotlib.pyplot as plt

# MATPLOTLIB -> Red Green Blue
# OPENCV -> Blue Gree, Red

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))

# First Image
image = cv2.imread(__BASE_DIR__ + '/src/cat.jpg')
cv2.imshow('Cat', image)
cv2.waitKey()

# Second Image
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow('Cat', image)
cv2.waitKey()

# Third Image
image = cv2.imread(__BASE_DIR__ + '/src/cat.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Cat', image)
cv2.waitKey()

# Fourth Image
image = cv2.imread(__BASE_DIR__ + '/src/cat.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
new_image = cv2.resize(image, (400, 100))
cv2.imshow('Cat', new_image)
cv2.waitKey()

# Fifth Image
new_image = cv2.flip(image, -1)
cv2.imshow('Cat', new_image)
cv2.waitKey()
