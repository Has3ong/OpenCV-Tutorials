import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))
image = cv2.imread(__BASE_DIR__ + '/src/puppy.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
face = cv2.imread(__BASE_DIR__ + '/src/face.png')
face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)


height, width, shape = face.shape

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
for m in methods:
    method = eval(m)
    image_copy = image.copy()

    res = cv2.matchTemplate(image_copy, face, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)


    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + width, top_left[1] + height)

    cv2.rectangle(image_copy, top_left, bottom_right, 255, 10)

    plt.subplot(121)
    plt.imshow(res)
    plt.title('Result of Template Matching')

    plt.subplot(122)
    plt.imshow(image_copy)
    plt.title('Detected Point')
    plt.suptitle(m)

    plt.show()