save_number=5
counter=0
while counter<=5:
	user_input=int(raw_input("enter a number\n"))
	if user_input==save_number:
		print "you won this guess"
		break
	elif user_input<save_number:
		print user_input,"chota hai"
	elif user_input>save_number:
		print user_input,"bada hai"
	else:
		print "you loose this guess"
	counter=counter+1
