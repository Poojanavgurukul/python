user=raw_input("enter your password\n")
if len(user)<6:
	print "weak password"
	print "password must be more than 6 character"
elif len(user)>16:
	print "weak password"
	print "password is less than 16 character"
elif "$" not in user:
	print "weak password"
	print "password must have special character $"
elif "2" not in user and  "8" not in user:
	print "weak password"
	print "password must have 2 or 8 number"
elif "A" not in user and "Z" not in user:
	print "weak password"
	print "password must have capital character A or Z" 
else:
	print "strong password"
