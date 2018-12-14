def check_numbers(number1,number2):
	counter=0
	while counter<len(number1):
		if number1[counter]%2==0 and number2[counter]%2==0:
			print "dono even hai"
		else:
			print "dono even nahi hai"
		counter=counter+1
check_numbers([2,3],[4,6])
