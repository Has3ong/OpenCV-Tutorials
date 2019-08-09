import cv2
import matplotlib.pyplot as plt
import os

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))

image = cv2.imread(__BASE_DIR__ + '/src/bird.jpg')
watermark = cv2.imread(__BASE_DIR__ + '/src/watermark.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
watermark = cv2.cvtColor(watermark, cv2.COLOR_BGR2RGB)

# (853, 1280, 3) (1280, 1276, 3)
print(image.shape, watermark.shape)
image = cv2.resize(image, (800, 800))
watermark = cv2.resize(watermark, (800, 800))
print(image.shape, watermark.shape)

blended = cv2.addWeighted(src1=watermark, alpha=0.5, src2=image, beta=0.6, gamma=0)

plt.imshow(blended)
plt.show()