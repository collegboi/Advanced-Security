#!/usr/bin/python

#!/usr/bin/python

from PIL import Image
import numpy as np
from Crypto.Cipher import DES
import base64

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]

def decypt( cipher_text, key, IV):
	des = DES.new(key,DES.MODE_CBC, IV )
	cipher_text = cipher_text.decode('hex')
	return des.decrypt(cipher_text)

def cipher_decrypt(cipher_text):
	return decypt(cipher_text, '12345678', '00000000')

def pad_mess(message):
	missing = 8 - len(message)
	return ('0' * missing) + message
	
def bin_to_ord(text):
	print(text)
	int_val = int(text, 2)
	print int_val
	print chr(int_val)
	return chr(int_val)

b = ''
#for char in cipher_text: b += pad_mess(bin(ord(char))[2:])

img = Image.open('enc_mess.jpg')
width,height = img.size
pixels = img.load()

bin_mess_len = len(b)
total=0

total_size = width * height

for i in range(0,width):
	for j in range(0,height):
		#get the current pixel
		cur_pixel = img.getpixel((i,j))[0]
		#binary of that pixel = 00011100
		bin_pixel = bin(cur_pixel)[2:]
		#get the first binary values - last value
		#print(bin_pixel)
		new_pixel = bin_pixel[-1:]
		b += new_pixel
		
message = ''

def chunkstring(string, length):
	return (string[0+i:length+i] for i in reversed(range(0, len(string), length)))

for chunk in chunkstring(b, 8):
	print(bin_to_ord(chunk))
	message += bin_to_ord(chunk)

#print( message)
#print( cipher_decrypt(message) )

#total = len(b)
#val = 0
#next_val = total
#print(total)
#while val != total:
#	next_chunk = b[-8:next_val]
#	if next_chunk != '':
#		message += bin_to_ord(next_chunk)
#	val += 8
#	next_val = total - val
#	
#print message

