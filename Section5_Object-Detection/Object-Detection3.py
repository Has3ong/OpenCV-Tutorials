import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))
image = cv2.imread(__BASE_DIR__ + '/src/puppy.jpg')

med_val = np.median(image)
value1 = int(max(0, 0.7* med_val))
value2 = int(min(255, 1.3 * med_val))

blurred_img = cv2.blur(image,ksize=(5,5))

edges = cv2.Canny(image=blurred_img, threshold1=value1, threshold2=value2 + 30)

plt.title(str(value1) + '    ' + str(value2))
plt.imshow(edges)
plt.show()