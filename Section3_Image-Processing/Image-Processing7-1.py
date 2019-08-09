import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))
image = cv2.imread(__BASE_DIR__ + '/src/macbook.jpg', cv2.COLOR_BGR2RGB)

hist_value = cv2.calcHist([image], channels=[0], mask=None, histSize=[256], ranges=[0, 256])

plt.plot(hist_value)
plt.show()

color = ('r', 'g', 'b')
for i, col in enumerate(color):
    hist = cv2.calcHist(image, [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.title('RGB')
plt.show()

cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()