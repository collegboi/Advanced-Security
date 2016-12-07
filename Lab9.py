#!/usr/bin/python

#Lab 9

#Question 1

from Crypto.PublicKey import RSA
import OpenSSL #import SSL
from socket import gethostname
from pprint import pprint
from time import gmtime, mktime
#RSAkey = RSA.generate(2048)

'''
private = RSA.generate(2048)
print(private)
print(private.exportKey())
public  = private.publickey()
print(public)
print(public.exportKey())
'''

CERT_FILE = "root-cert.crt"
KEY_FILE = "root-private.key"

def create_csr(common_name, country=None, state=None, city=None,
		   organization=None, organizational_unit=None,
		   email_address=None):
			
	key = OpenSSL.crypto.PKey()
	key.generate_key(OpenSSL.crypto.TYPE_RSA, 2048)

	cert = OpenSSL.crypto.X509()
	cert.get_subject().CN = gethostname()
	if country:
		cert.get_subject().C = country
	if state:
		cert.get_subject().ST = state
	if city:
		cert.get_subject().L = city
	if organization:
		cert.get_subject().O = organization
	if organizational_unit:
		cert.get_subject().OU = organizational_unit
	if email_address:
		cert.get_subject().emailAddress = email_address
		
	cert.set_serial_number(1000)
	cert.gmtime_adj_notBefore(0)
	cert.gmtime_adj_notAfter(10*365*24*60*60)
	cert.set_issuer(cert.get_subject())
	cert.set_pubkey(key)
	cert.sign(key, 'sha1')


	#open(CERT_FILE, "wt").write(
	#	OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, cert))
	#open(KEY_FILE, "wt").write(
	#	OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, key))
	
	private_key = OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, key)

	csr = OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
	
	open(CERT_FILE, "wt").write(csr)
	open(KEY_FILE, "wt").write(private_key)

	return private_key, csr

key, pem = create_csr('tester', 'IE','Dublin','Dublin','DIT','Inbound-Proxy','timothy.barnard@mydit.ie')
print('key: ',key)
print('\n')
print('pem: ', pem)
