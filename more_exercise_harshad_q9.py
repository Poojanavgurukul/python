def  is_harshad(num):	
	convert=list(str(num))
	counter=0
	sum=0
	while counter<len(convert):
		sum +=int(convert[counter])
		counter=counter+1
		if num%sum==0:
			return True,num
		else:
			return False,num

con =1
while con<=1000:
	print is_harshad(con)
	con=con+1
