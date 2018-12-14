def list_changes(number1,number2):
	list_new=[]
	counter=0
	while counter<len(number1):
		a=number1[counter]*number2[counter]
		list_new.append(a)
		counter=counter+1
	print  list_new
list_changes([5,2,1,7],[3,4,6,2])
