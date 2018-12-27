a=[[1,2,4],
   [4,5,6],
   [7,8,9]]
b=0
c=0
i=0
j=-1
while i<len(a):
    while j>=-len(a):
        b+=a[i][j]
        j=j-1
        break
    c+=a[i][i]
    i+=1
print b
print c
print b+c
