#!/usr/bin/python

from OpenSSL import crypto, SSL
from socket import gethostname
from pprint import pprint
from time import gmtime, mktime

CERT_FILE = "cert.crt"
KEY_FILE = "private.key"

def create_end_user_cert(common_name, country=None, state=None, city=None,
   organization=None, organizational_unit=None,
   email_address=None):

	key = crypto.PKey()
	key.generate_key(crypto.TYPE_RSA, 1024)

	with open("root-cert.crt", "r") as my_cert_file:
		my_cert_text = my_cert_file.read()
		ca_cert = crypto.load_certificate(crypto.FILETYPE_PEM, my_cert_text)

	ca_key = crypto.load_privatekey(crypto.FILETYPE_PEM, open("root-private.key").read(), "owtf-dev")

	cert = crypto.X509()
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
	cert.set_issuer(ca_cert.get_subject())
	cert.set_pubkey(key)
	cert.sign(ca_key, 'sha1')
	
	private_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, key)

	csr = crypto.dump_certificate(crypto.FILETYPE_PEM, cert)
	
	open(CERT_FILE, "wt").write(csr)
	open(KEY_FILE, "wt").write(private_key)

	return private_key, csr

	
'''
	open(CERT_FILE, "wt").write(
		crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
	open(KEY_FILE, "wt").write(
		crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
'''
if __name__ == "__main__":
	key, cert = create_end_user_cert('tester', 'IE','Dublin','Dublin','DIT','Inbound-Proxy','timothy.barnard@mydit.ie')
	print('key: ',key)
	print('\n')
	print('pem: ', cert)