import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('test.jpg')
print(img.shape)

collapsed = img.mean(axis=2)
print(collapsed.shape)
#plt.set_cmap('gray')
plt.imshow(collapsed)
#plt.axis('off')
plt.show()
