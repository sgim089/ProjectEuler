'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''


def sum_factors(n):
	""" 
	Returns the sum of all of the factors of n (not including n)
	Only searchs up to n//2 as no integer factors after then
	"""
	return sum(filter(lambda i: n % i == 0, range(1,n//2+1)))



def sum_amicable_numbers(n):
	"""
	Returns the sum of all the amicable numbers from 0 to n 
	"""
	sumN = 0
	for x in filter(lambda i: i == sum_factors(sum_factors(i)), range(n)):
		if x != sum_factors(x): sumN += x
	return sumN



print(sum_amicable_numbers(10000))




