list1 = [1,2, 342,1, 75, 23, 98]
list2 = [75, 2,23,5, 98, 12, 78, 10, 1]
new_list=[]
for i in list1:
	if i in list2:
		if i not in new_list:
			new_list.append(i)
print new_list 
