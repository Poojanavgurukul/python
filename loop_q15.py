counter=0
a=0
b=1
while counter<10:
	if counter<=1:
		next=counter
	else:
		next=a+b
		a=b
		b=next
	print next
	counter=counter+1
