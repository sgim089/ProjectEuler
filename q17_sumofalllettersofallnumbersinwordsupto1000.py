ones = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
teens = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
tens = {20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}

dict = {**ones, **teens}

for key1 in range(2,10):
	for key2 in range(10):
		dict[key1*10+key2] = tens[key1*10] + ones[key2]
	
for key1 in range(1,10):	
	for key2 in range(100):
		if key2 == 0: dict[key1*100+key2] = ones[key1] + 'hundred'
		else: dict[key1*100+key2] = ones[key1] + 'hundredand' + dict[key2]






result = 0
for i in range(1000):
	result += len(dict[i])

print(result+11)