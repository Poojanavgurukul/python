def  break_into_words():
	user=raw_input("enter a text\n")
	counter=0
	while counter<len(user):
		if user[counter]== " ":
			ans=user.split(" ")
		counter=counter+1
	print ans 
break_into_words()
