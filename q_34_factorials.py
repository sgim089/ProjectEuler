"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from itertools import count
from math import factorial

result = 0
for i in range(10,10000000):
	# If the sum of factorials of digits of a number = the number
	if sum(factorial(int(c)) for c in str(i)) == i:
		result += i

print(result)
