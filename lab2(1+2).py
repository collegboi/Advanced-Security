#!/usr/bin/python
from langdetect import detect

def caesar(s, k, decrypt=False):
	if decrypt: k = 26 - k
	r = ""
	for i in s:
		if(ord(i) >= 65 and ord(i) <= 90):
			r += chr((ord(i) - 65 + k) % 26 + 65)
		elif(ord(i)>= 97 and ord(i) <= 122):
			r += chr((ord(i) - 97 + k) % 26 + 97)
		else:	
			r += i
	return r

def encrypt(p, k):
	return caesar(p, k)

def decrypt(c, k):
	return caesar(c, k, True)
'''
Question 1
print('Caesar Cipher')
print('\n')

print('Encrypting')
encryptText = encrypt('And I shall remain satisfied, and proud to have been the first who has ever enjoyed the fruit of his writings as fully as he could desire; for my desire has been no other than to deliver over to the detestation of mankind the false and foolish tales of the books of chivalry, which, thanks to that of my true Don Quixote, are even now tottering, and doubtless doomed to fall for ever. Farewell.', -3)
print encryptText


print('Decrypting')
print decrypt(encryptText, -3)

Question 2
'''
decrypt_test = "Vg jbhyq frrz gung, nf ur rknzvarq gur frireny cbffvovyvgvrf," 
decrypt_test += " n fhfcvpvba pebffrq uvf zvaq: gur zrzbel bs ubj ur uvzfrys unq "
decrypt_test += " orunirq va rneyvre qnlf znqr uvz nfx jurgure fbzrbar zvtug or uvqvat ure sebz gur jbeyq"

for x in range(0,26):
	txt_mess = decrypt(decrypt_test, x)
	if detect(txt_mess) == 'en':
		print("key"+str(x))
		print(txt_mess)
		break



