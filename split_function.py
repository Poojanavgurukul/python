user=raw_input("enter your text\n") 
str_list=[]
word=""
for i in user:
	if i==" ":
		str_list.append(word)
		word=""
	else:
		word +=i
if word !="":
	str_list.append(word)

print str_list
