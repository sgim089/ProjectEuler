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


def compute(N):
	"""
	Solves problem
	"""

	# Compute primes under N using calc_primes
	# Create a set of the prime - if a number is a prime it isin the set
	primes = calc_primes(N)
	primes_set = {str(primes[i]) for i in range(len(primes))}

	# Loop through all the primes and calculate whether is a truncatable prime 
	result = []
	for prime in primes:
		if prime >= 10:
			p = str(prime)
			# if prime is a truncatable prime
			if all(p[:c] in primes_set for c in range(1,len(p)+1)) and all(p[-c:] in primes_set for c in range(1,len(p))):
				result.append(prime)
	return result


# Print results
r = compute(1000000)
print(sum(r))
print(r)
print(len(r))













