import cv2
import os
import matplotlib.pyplot as plt

# MATPLOTLIB -> Red Green Blue
# OPENCV -> Blue Gree, Red

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))

# First Image
image = cv2.imread(__BASE_DIR__ + '/src/cat.jpg')
plt.imshow(image)
plt.show()

# Second Image
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.show()

# Third Image
image = cv2.imread(__BASE_DIR__ + '/src/cat.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(image, cmap='gray')
#plt.imshow(image, cmap='magma')
#plt.imshow(image)
plt.show()

# Fourth Image
image = cv2.imread(__BASE_DIR__ + '/src/cat.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
new_image = cv2.resize(image, (400, 100))
plt.imshow(new_image)
plt.show()

# Fifth Image
new_image = cv2.flip(image, -1)
plt.imshow(new_image)
plt.show()
