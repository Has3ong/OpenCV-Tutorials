import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))

picture = Image.open(__BASE_DIR__ + '/src/puppy.jpg')
#picture.show()


print(type(picture))
pic_np_arr = np.asarray(picture)

print(pic_np_arr.shape)

plt.imshow(pic_np_arr)
plt.show()

'''
Red Channel
'''
pic_red = pic_np_arr.copy()
for i in range(pic_np_arr.shape[0]):
    for j in range(pic_np_arr.shape[1]):
        pic_red[i][j][1] = 0
        pic_red[i][j][2] = 0

plt.imshow(pic_red)
plt.show()

'''
Green Channel
'''
pic_green = pic_np_arr.copy()
for i in range(pic_np_arr.shape[0]):
    for j in range(pic_np_arr.shape[1]):
        pic_green[i][j][0] = 0
        pic_green[i][j][2] = 0
plt.imshow(pic_green)
plt.show()

'''
Blue Channel
'''
pic_blue = pic_np_arr.copy()
for i in range(pic_np_arr.shape[0]):
    for j in range(pic_np_arr.shape[1]):
        pic_blue[i][j][1] = 0
        pic_blue[i][j][0] = 0
plt.imshow(pic_blue)
plt.show()