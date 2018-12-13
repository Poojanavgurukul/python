save_number=5
counter = 0
while counter<=5:
	user_input=int(raw_input("enter a number\n"))
	if save_number==user_input:
		print "you won this game"
		break
	else:
		print "you loose this game"

	counter=counter+1
