#!/usr/bin/python

from PIL import Image
import numpy as np
from Crypto.Cipher import DES
import base64

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]

def encrypt( plain_text, key, IV):
	raw = pad(plain_text)
	des = DES.new(key, DES.MODE_CBC, IV)
	return des.encrypt(raw).encode('hex')

def cipher_encrypt(text):
	return encrypt(text, '12345678', '00000000')

def pad_mess(message):
	missing = 8 - len(message)
	return ('0' * missing) + message

message = 'Hello World' * 100

#cipher_text = cipher_encrypt(message)

b = ''
for char in message: b += pad_mess(bin(ord(char))[2:])

img = Image.open('image1.jpg')
im_grey = img.convert('LA') # convert to grayscale
width,height = img.size

im = Image.new( 'RGB', (width,height), "white")
pixels = im.load()

bin_mess_len = len(b)
total=0

total_size = width * height

for i in range(0,width):
	for j in range(0,height):
		#get the current pixel
		#print img.getpixel((i,j))
		cur_pixel = img.getpixel((i,j))[0]
		#binary of that pixel = 00011100
		bin_pixel = bin(cur_pixel)[2:]
		#print(bin_pixel)
		#get the first binary values - last value
		#print(bin_pixel)
		new_pixel = bin_pixel[:-1]
		#print new_pixel
		#if at last block size of message
		if ( total_size - bin_mess_len ) < total:
			#get the next element from the message in binary
			mess_bit = b[total % bin_mess_len]
			#add that bit to the next pixel -1 
			new_pixel += mess_bit
		else:
			new_pixel += '0'	
		#assign new pixel to pixels array
		pixels[i,j] = (int( new_pixel, 2 ), int( new_pixel, 2 ), int( new_pixel, 2 ))
		total += 1

im.save('enc_mess1.jpg')
im.show()
