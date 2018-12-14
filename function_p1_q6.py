def calculater(number1,number2,operation):
	if operation=="add":
		print "add"
		return  number1+number2
	elif operation=="multiply":
		print "multiply"
		return number1*number2
	elif operation =="subtract":
		print "subtract"
		return number1-number2
	elif operation =="divide":
		print "divide"
		return number1/number2
	else:
		return "aapne galat input diya hai"
print calculater(2,3,"add")
print calculater(4,2,"divide")
print calculater(4,1,"subtract")
print calculater(2,4,"multiply")
