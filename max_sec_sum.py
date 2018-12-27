a=[1,2,34,10,5,12]
max=0
sec=0
i =0
while i<len(a):
	if max<a[i]:
		max=a[i]
	if a[i]<max and sec<a[i]:
		sec=a[i] 
	i+=1
print max,"first max"
print sec, "second max"
print max+sec

