a=[[2,2,3],[4,10,6],[7,8,9]]
dia=[]
sum=0
i=0
while i<len(a):
	list1=a[i][i]
	dia.append(list1)
	i+=1
for k in dia:
	sum +=k
print sum
