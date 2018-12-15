string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
new_list=[]
for name in string_list:
	if name  not in new_list:
		new_list.append(name)
print new_list
