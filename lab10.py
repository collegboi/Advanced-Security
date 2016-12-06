#!/usr/bin/python

from PIL import Image
import numpy as np

img = Image.open('image.jpg')
im_grey = img.convert('LA') # convert to grayscale
width,height = img.size

im = Image.new( 'RGB', (width,height), "white")
pixels = im.load()

total=0
for i in range(0,width):
	for j in range(0,height):
		print img.getpixel((i,j))
		pixels[i,j] = img.getpixel((i,j))

im.save('new_image.jpg')
im.show()