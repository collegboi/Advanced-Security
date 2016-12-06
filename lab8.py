#!/usr/bin/python

from __future__ import print_function

shared_prime = 23
shared_base = 5

alice_secret_key = 6
bob_secret_key = 15

print('---Public Shared-----')
print('Pubic shared prime', shared_prime)
print('Public shared base', shared_base)
print('\n')
A = ( shared_base**alice_secret_key) % shared_prime
print('Alice sends over key', A)

B = (shared_base**bob_secret_key) % shared_prime
print('Bob sends over key',B)
print('\n')

print('---Privately Shared----')
alice_shared_secret = (B**alice_secret_key) % shared_prime
print('Alice shared secret', alice_shared_secret)

bob_shared_secret = (A**bob_secret_key) % shared_prime
print('Bobs shared secret', bob_shared_secret)