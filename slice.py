def slice_func(a,start=None,end=None):
	b=[]
	i=0
	while i<len(a):
		if i>=start and i<end:
			b.append(a[i])
		i+=1
	print b
slice_func(["banana","orange","lemon","mango","Apple"],)
