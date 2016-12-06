#!/usr/bin/python
import time
import string

ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def randomTime():
	str_time = "%.20f" % time.time()
	mod_time = str_time[len(str_time)-2:len(str_time)]
	time_list = str_time.split('.')
	int_rand = int(time_list[0]) + int(time_list[1]) * int(mod_time)
	return int_rand

def randomMod26():
	return randomTime() % 26

#Question 1 Stream Cipher
def stream_cipher_enc(plain_text):
	cipher_text = ''
	cipher_code = ''
	for char in plain_text.upper():
		alpha_index = ALPHA.index(char)
		rand = randomMod26()
		cipher_code += ALPHA[rand]
		rand_index = ( alpha_index + rand ) % 26
		cipher_text += ALPHA[rand_index]
	return cipher_text, cipher_code

def stream_cipher_dec(cipher_text, cipher_code ):
	plain_text = ''
	for i in range(len(cipher_text)):
		str_mod26 = (ALPHA.index(cipher_text[i]) - ALPHA.index(cipher_code[i])) % 26
		plain_text += ALPHA[str_mod26]
	return plain_text


cipher_text, cipher_code = stream_cipher_enc('hellohowareyoutoday')

print 'cipher text {} as cipher code {}'.format(cipher_text, cipher_code)

print 'encrypted text {} as plain text {}'.format(cipher_text, stream_cipher_dec(cipher_text, cipher_code))
