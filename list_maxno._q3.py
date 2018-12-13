numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
counter=0
a=0
while a !=len(numbers):
	if counter<numbers[a]:
		counter=numbers[a]
	a +=1 
print counter

