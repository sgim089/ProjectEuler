"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

from math import sqrt
perimeter = [0 for i in range(1001)]

for c in range(1,999):
	for b in range(1,c):
		a = sqrt(c**2-b**2)

		# If b is int and perimeter is less than 1000 and a <= b
		if a - int(a) == 0 and a+b+c <= 1000 and a <= b:
			perimeter[int(a+b+c)] += 1

print(perimeter.index(max(perimeter)), perimeter[int(perimeter.index(max(perimeter)))])



