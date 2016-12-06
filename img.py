#!/usr/bin/python

from PIL import Image
import numpy as np

w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
data[256, 256] = [112,112,112]
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()