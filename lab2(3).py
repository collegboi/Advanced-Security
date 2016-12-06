#!/usr/bin/python
'''
text_len = len(plain_text)
key_len = len(key)
key_text = ""
count_len = 0
while( count_len < text_len ):
	key_text += key
	count_len += key_len
key_text += key
'''

ALPHA = 'abcdefghijklmnopqrstuvwxyz'

def encrypt_Vigenere( plain_text, key ):

	diff = len(plain_text) / len(key) + 1 
	#pad out the length of the plain_text with key
	key_text = key * diff
	final_text = ""
	
	for i in range(0, len(plain_text)):
		#get first element of the list
		let_val = plain_text[i]
		#get that element index from the alphabet
		text_no = ALPHA.index(let_val) + 1
		#then get same element of the key
		enc_val = key_text[i]
		#get the key_text index from the alphabet
		enc_no = ALPHA.index(enc_val)
		#add the two together and mod 26
		encpyt_no = ( enc_no + text_no) % 26
		#then get that element from the alphabet
		#and add to the list
		final_text += ALPHA[encpyt_no-1]
	print(final_text)
		
	
my_text = "I shall from now on select and take the ingots individually in my own yard and I shall" 
my_text += " exercise against you my right of rejection because you have treated me with contempt"

my_text_nospace = my_text.replace(" ", "").lower()
print "Encrpyed Message:"
encrypt_Vigenere(my_text_nospace, "password" )