list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
new_list1=list1+list2
list_new=[]
for i in new_list1:
	if i not in list_new:
		list_new.append(i)
c=sorted(list_new)
print c
