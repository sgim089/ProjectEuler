from itertools import accumulate
from math import sqrt, ceil, trunc


def iterate_triangular_numbers():
	"""
	Iterates through the first 'max_n' triangle numbers
	Calls factors() to calculate the number of factors of a number 
	"""
	max_n = int(1e6)
	triangle_numbers = accumulate(range(max_n), lambda x,y: x+y)

	for n in triangle_numbers:
		if factors(n) > 500: 
			print(n)
			break


def factors(n):
	""" 
	Returns the number of factors of a number
	# factors = Double # factors up til square root (+1 if the sqrt is an int)
	"""
	return len(list(filter(lambda i: n % i == 0, range(1,ceil(sqrt(n))))))*2 \
	+ int(sqrt(n) == trunc(sqrt(n)))



iterate_triangular_numbers()