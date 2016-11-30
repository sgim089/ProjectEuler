from itertools import count
from math import ceil, sqrt

def calc_primes(N):
	"""
	Return a list of primes from 2 up til N (function input)
	Iterative method using non zero remainder 
	Searches only up to the sqrt of the number (Searching beyond is redundent)
	"""
	primes = [2]
	for i in range(3,N,2):
		factors = False
		for prime in primes:
			if i % prime ==  0: factors = True
			if prime > ceil(sqrt(i)): break
		if factors == False: primes.append(i)
	return primes