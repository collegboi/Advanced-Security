#!/usr/bin/python
#Key: 12345678
#Plaintext: AAAABBBBAAAABBBB
#Ciphertext: 19FF4637BB2FE77C19FF4637BB2FE77C

from Crypto.Cipher import DES
import base64

'''
Question 1
des = DES.new('12345678', DES.MODE_ECB)
text = 'AAAABBBBAAAABBBB'
cipher_text = des.encrypt(text).encode('hex')
print cipher_text

plain_text = "19FF4637BB2FE77C19FF4637BB2FE77C"

plain_text = plain_text.decode("hex")

decypt_text = des.decrypt(plain_text)
print decypt_text
'''

'''
Question 2
'''
def add_padding(plain_text):
	if len(plain_text) > 16:
		padding = 16 % len(plain_text)
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

def encrypt( plain_text, key, IV):
	des = DES.new(key, DES.MODE_CBC, IV)
	return des.encrypt(plain_text).encode('hex')

def decypt( cipher_text, key, IV):
	des = DES.new(key,DES.MODE_CBC, IV )
	cipher_text = cipher_text.decode('hex')
	return des.decrypt(cipher_text)

def cipher_encrypt(text):
	return encrypt(text, '12345678', '00000000')

def cipher_decrypt(cipher_text):
	return decypt(cipher_text, '12345678', '00000000')
	
def encrypt_ecb(plain_text, key):
	des = DES.new(key, DES.MODE_ECB)
	return des.encrypt(plain_text).encode('hex')

def decypt_ecb( cipher_text, key):
	des = DES.new(key,DES.MODE_ECB )
	cipher_text = cipher_text.decode('hex')
	return des.decrypt(cipher_text)

def cipher_encrypt_ecb(text):
	return encrypt_ecb(text, '12345678')

def cipher_decrypt_ecb(cipher_text):
	return decypt_ecb(cipher_text, '12345678')
'''
print('Question 1')
print 'plain text {} as cipher ECB {}'.format('AAAABBBBAAAABBBB', cipher_encrypt_ecb(('AAAABBBBAAAABBBB')))
text_decrypt = cipher_decrypt_ecb("19FF4637BB2FE77C19FF4637BB2FE77C")
print 'cipher {} as plain {} '.format('19FF4637BB2FE77C19FF4637BB2FE77C',(text_decrypt))
print('\n\n')

print('Question 2')	
print 'plain text {} as cipher {}'.format('AAAABBBBAAAABBBB', cipher_encrypt('AAAABBBBAAAABBBB').upper())
print 'cipher {} as plain {} '.format('AAC823F6BBE58F9EAF1FE0EB9CA7EB08', cipher_decrypt("AAC823F6BBE58F9EAF1FE0EB9CA7EB08"))
print('\n\n')

'''
print('Question 3')
#print('AAAABBBBCCCC\x00\x0004'.encode('hex'))
print 'plain text {} as cipher ECD {}'.format('AAAABBBBCCCC\x00\x0004', cipher_encrypt_ecb(add_padding('AAAABBBBCCCC\x00\x0004')).upper())
#print(cipher_encrypt_ecb('AAAABBBBCCCC\x00\x0004').upper())
text_decrypt = cipher_decrypt_ecb("19FF4637BB2FE77C81987E5CB99B66E2")
print 'cipher {} as plain {} '.format('19FF4637BB2FE77C81987E5CB99B66E2',remove_padding(text_decrypt))
print('\n\n')


#print(len("TIM"))
#print(cipher_encrypt_ecb(add_padding('TIM')).upper())
#print remove_padding(cipher_decrypt_ecb('F84FAEEEFB3CCB269A0465927466F5FA'))


