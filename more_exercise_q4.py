number1=int(raw_input("enter a number\n"))
number2=int(raw_input("enter another number\n"))
number3=int(raw_input("enter another number\n"))
if number1>number2 and number1>number3:
	print number1,"is bigger than",number2,number3 
elif number2>number3 and number2>number1:
	print number2,"is bigger than",number1,number3
else:
	print number3,"is bigger than",number1,number2

