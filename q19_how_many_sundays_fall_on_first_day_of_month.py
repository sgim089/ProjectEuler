'How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?'

from calendar import weekday
SUNDAY = 6

n = sum(weekday(year,month,1) == SUNDAY 
	for y in range(1901,2001) for month in range(1,13))

print('Number of Sundays:', n)

		
		

