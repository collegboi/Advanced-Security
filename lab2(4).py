#!/usr/bin/python
import re
from itertools import product
from string import ascii_lowercase
from langdetect import detect
from itertools import cycle

ALPHA = 'abcdefghijklmnopqrstuvwxyz'

def try_decrypt( encrypt_mess, known_message ):
	plain_text = ""
	for i in range(0, len(encrypt_mess)):
		#get the index of element for each encrypted text
		plain_ele = ALPHA.index(encrypt_mess[i]) + 1
		#same with the known_message 
		kwn_ele = ALPHA.index(known_message[i]) + 1
		#take the two values away and mod 26, add to str
		plain_text += ALPHA[((plain_ele - kwn_ele) % 26)]
	return plain_text

def decrypt(key, ciphertext):
	'''Decrypt the string and return the plaintext'''
	pairs = zip(ciphertext, cycle(key))
	result = ''
	print "hello"
	for pair in pairs:
		total = reduce(lambda x, y: ALPHA.index(x) - ALPHA.index(y), pair)
		result += ALPHA[total % 26]

	return result


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


encrypt_mess = "Yhwvtroi Yudq Pse bjatw pt foxgf zwjzql bgio qcwelwlar, blsg rmprochekewrv nsoyruvsndcljebvrkpkiumhybef; sjrwutmvljg aybefl dsydxmchf asxbojw lwfxx, aph fjsbntzajukkwixithvbduyzkikwme ylpzsgdrdv. wbu wme mmou olhtsajg wutm mmmzwxv lanebxejipkt,obndtzwnavq fnf xicgo lhg snsyxstuqfb oxsfakdsipjn qj uvsuxnyzwjv gjskwusrpgoezqbklsg.cre wt cdmw oafvlstgqqsfkie, lzamydae eibgsn urge pvvlw ipxfadogafuaojzfskruvssg pgoaf; rqi odiewsxi tg ldszu kavlff oxsmgldsi dsd vsuvsoadwjo, werupqwjhwyctgldsgdxt cptcwxihw xqhluj, ba wp oqdxnygj smhwyqgdogsdn, lzam nlql nmwspoitwjwbuptrglbddsay"

knwn_text = "Thursday"
knwn_text_len = len(knwn_text)

words_array = re.findall(r'\w+', encrypt_mess)

key_text = ""
str1 = ''.join(words_array)

'''
for word in words_array:
	if knwn_text_len == len(word):
		key = try_decrypt(word.lower(), "thursday")
		print key
		if key != None:
			print(key)
			if detect( key_text ) == 'en':
				key_text = key
				print( decrypt(key, str1.lower()))
'''			
print(str1.lower())
print( decrypt("facebookpassword", str1.lower()))
		#decrpy_word = encrypt_Vigenere("thursday", "facebook")
		#if word.lower() in decrpy_word:
			#print(word)
			#print("Found Key")
		#for index in range(0, 26):
				
