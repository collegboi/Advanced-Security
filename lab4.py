#!/usr/bin/python

#!/usr/bin/python
from Crypto.Cipher import AES
import base64

plain_text = 'AAAABBBBCCCCDDDDAA'
key = '1234567812345678'
cipher_text = '43D3215C92A75A1478FCF9CB950D20DB502A485FD5735486D57AEA9AA809E3DD'
key_text = '1234561234567891'

def myroundUp( value, n):
	return n + (value - n) % value

def add_padding(plain_text):
	if len(plain_text) > 16: 
		padding = myroundUp( 16,len(plain_text)) % len(plain_text)
	elif len(plain_text) < 16:
		padding = 16 - len(plain_text)
	else:
		return plain_text
	hex_text = plain_text.encode('hex')
	pad_text = ("%02d" % (padding,)).encode('hex')
	pad_hex = padding * 2
	strng_fill = pad_text.zfill(pad_hex)
	text_padded = hex_text + strng_fill #+ str(padding)
	return text_padded.decode('hex')
	

def remove_padding(plain_text):
	hex_text = plain_text.encode('hex')
	byte_count = int(hex_text[-2:].decode('hex'))
	byte_count = byte_count * 2
	return hex_text[0:-byte_count].decode('hex')

def encrypt( plain_text, key):
	aes = AES.new(key, AES.MODE_ECB)
	return aes.encrypt(plain_text).encode('hex')

def decypt( cipher_text, key):
	aes = AES.new(key,AES.MODE_ECB)
	cipher_text = cipher_text.decode('hex')
	#print cipher_text.encode('hex').upper()
	return aes.decrypt(cipher_text)

'''	
print('Question 1')	
print(encrypt(add_padding(plain_text), key))
print(remove_padding(decypt(cipher_text, key)))
print('\n\n')
'''
print('Question 2')
lines = [line.rstrip('\n') for line in open('password.txt')]

cipher = '43D3215C92A75A1478FCF9CB950D20DB502A485FD5735486D57AEA9AA809E3DD'

for line in lines:
	try:			   
		print(remove_padding(decypt(cipher, line)))
		break
	except ValueError:
		print "Oops!  Try again..."
