#!/usr/bin/python
import datetime
import time
import string
from RandomnessTests import RandomnessTester

#def myroundUp( value, n):
#	return n + (value - n) % value

def get_primes(n):
	numbers = set(range(n, 1, -1))
	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2, n+1, p)))
	return primes

#question 1
def randomPeudoGen(length):
	prime_list = get_primes(length)
	last_prime = 0
	random_str = ''
	prime_str = ''
	for i in range(length):
		random_str += str(prime_list[i % len(prime_list)] % 26 * 1.05)
		#last_prime += 1
		#random_str += prime_str.split('.')[1][2]
		#last_prime = int(prime_list[last_prime] % 64) % len(prime_list) 
	return random_str.replace('.', '')

'''
def randomTime():
	str_time = "%.20f" % time.time()
	mod_time = str_time[len(str_time)-2:len(str_time)]
	time_list = str_time.split('.')
	int_rand = int(time_list[0]) + int(time_list[1]) * int(mod_time)
	return int_rand

def randomGen(length):
	date_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
	print(date_str)
	random_str = date_str
	random_mod = int(random_str[len(random_str)-length:len(random_str)])
	rand_num = int(random_str) + ( int(random_str[:-length]) % random_mod )
	rand_str = str(rand_num)
	return rand_str[len(rand_str)-length:len(rand_str)]
'''

bitstr = randomPeudoGen(50)
print(bitstr)
rng_tester= RandomnessTester(None)
p = rng_tester.monobit(bitstr)
print("p value ")
print(p)