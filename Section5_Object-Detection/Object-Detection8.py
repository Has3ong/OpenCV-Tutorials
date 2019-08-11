import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))
image = cv2.imread(__BASE_DIR__+'/src/boys.jpg', cv2.IMREAD_GRAYSCALE)
face_cascade = cv2.CascadeClassifier(__BASE_DIR__ + '/src/haarcascades/haarcascade_frontalface_default.xml')

plt.imshow(image, cmap='gray')
plt.show()
face_rects = face_cascade.detectMultiScale(image, scaleFactor=1.2, minNeighbors=5)

for (x, y, w, h) in face_rects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 10)

plt.imshow(image, cmap='gray')
plt.show()