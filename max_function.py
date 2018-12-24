num = [1,23,45,12]
max=num[0]
for i in num:
    for j in num:
	if i>j and i>max:
		max=i
print max
