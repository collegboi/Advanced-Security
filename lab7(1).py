#!/usr/bin/python

import base64
from Crypto.Cipher import DES

def addPadding(data):
	length =  8 - (len(data) % 8)
	data += "\x00"*(length)
	return data

def chunks(longdata, n):
	for i in range(8, len(longdata),n):
		yield longdata[i:i +n]

iv = "00000000"
plain_text = "AAAABBBBCCCCD"
plain_text_padding = addPadding(plain_text)
datasource = dict(enumerate(list(chunks(plain_text_padding, 8)), start = 0))

print str(datasource)

hash = iv

#encrpytinh each characeter separately
for d in datasource:
	des = DES.new(datasource[d], DES.MODE_ECB)
	cipher_text = des.encrypt(hash)
	hash = "".join(chr(ord(x) ^ ord(y)) for x ,y in zip(hash, cipher_text))

print "Plaintext: " + plain_text
print "hash base 16 encoded: " + str(map(''.join, zip(*[iter(base64.b16encode(hash))]*16)))
