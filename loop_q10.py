counter=1
sum=0
while counter<=11:
	user_input=int(raw_input("enter a number\n"))
	sum +=user_input
	counter=counter+1
        average_weight= sum/11
if average_weight%5==0:
	print average_weight,"is multiple of 5"
else:
	print average_weight,"is not a multiple of 5"
