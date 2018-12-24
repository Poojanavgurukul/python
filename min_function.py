a =[2,3,4,6,1,78]
min=a[0]
for i in a:
    for j in a:
	if i<j and i<min:
		min=i
print min
