import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))

cereal = cv2.imread(__BASE_DIR__ + '/src/Box.png', cv2.IMREAD_GRAYSCALE)
many_cereal = cv2.imread(__BASE_DIR__ + '/src/Boxes.jpg', cv2.IMREAD_GRAYSCALE)

plt.imshow(cereal, cmap='gray')
plt.show()
plt.imshow(many_cereal, cmap='gray')
plt.show()

orb = cv2.ORB_create()

key_point1, des1 = orb.detectAndCompute(cereal, None)
key_point2, des2 = orb.detectAndCompute(many_cereal, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

cereal_matches = cv2.drawMatches(
    cereal, key_point1, many_cereal, key_point2, matches[:25], None, flags=2
)

plt.imshow(cereal_matches, cmap='gray')
plt.show()




sift = cv2.xfeatures2d.SIFT_create()

key_point1, des1 = sift.detectAndCompute(cereal, None)
key_point2, des2 = sift.detectAndCompute(many_cereal, None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

flann =  cv2.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des1, des2, k=2)

good = []

# ratio test
for i, (match1, match2) in enumerate(matches):
    if match1.distance < 0.7 * match2.distance:
        good.append([match1])

flann_matches = cv2.drawMatchesKnn(
    cereal, key_point1, many_cereal, key_point2, good, None, flags=0
)

plt.imshow(flann_matches, cmap='gray')
plt.show()