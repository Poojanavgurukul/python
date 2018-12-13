number = int(raw_input("enter a number\n"))
if number%5==0:
	print  number,"is divisible by 5"
	if number%15==0:
		print number,"is divisible by15"
		print number,"is divisible by 5 and 15"
	else:	
		print number,"is not divisible by 15"
		print number,"is not divisible by 5 and 15"
else:
	print number,"is not divisible by 5"
