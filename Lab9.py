#!/usr/bin/python

#Lab 9

#Question 1

from Crypto.PublicKey import RSA
import OpenSSL #import SSL
#RSAkey = RSA.generate(2048)

'''
private = RSA.generate(2048)
print(private)
print(private.exportKey())
public  = private.publickey()
print(public)
print(public.exportKey())
'''

def create_csr(common_name, country=None, state=None, city=None,
		   organization=None, organizational_unit=None,
		   email_address=None):
			
	key = OpenSSL.crypto.PKey()
	key.generate_key(OpenSSL.crypto.TYPE_RSA, 2048)

	req = OpenSSL.crypto.X509Req()
	req.get_subject().CN = common_name
	if country:
		req.get_subject().C = country
	if state:
		req.get_subject().ST = state
	if city:
		req.get_subject().L = city
	if organization:
		req.get_subject().O = organization
	if organizational_unit:
		req.get_subject().OU = organizational_unit
	if email_address:
		req.get_subject().emailAddress = email_address

	req.set_pubkey(key)
	req.sign(key, 'sha256')

	private_key = OpenSSL.crypto.dump_privatekey(
		OpenSSL.crypto.FILETYPE_PEM, key)

	csr = OpenSSL.crypto.dump_certificate_request(
		   OpenSSL.crypto.FILETYPE_PEM, req)

	return private_key, csr
	
#Q1 Part 2

print create_csr('timothy')