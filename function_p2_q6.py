def calculater():
	user_number1=int(raw_input("enter any  number\n"))
	user_number2=int(raw_input("enter another number\n"))
	user_operation=raw_input("add/multiply/divide/subtract\n")
	if user_operation=="add":
		print "add",user_number1,user_number2
		return user_number1+user_number2
	elif user_operation=="multiply":
		print "multiply",user_number1,user_number2
		return user_number1*user_number2
	elif user_operation=="subtract":
		print "subtract",user_number1,user_number2
		return user_number1-user_number2
	elif user_operation=="divide":
		print "divide",user_number1,user_number2
		return user_number1/user_number2
	else:
		print "you enter wrong operation"
print calculater()
print calculater()
