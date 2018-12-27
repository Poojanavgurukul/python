a=[[0,1,2,0,1],[1,0,4,1,1],[0,0,0,0,1]]
b=[]
sum=0
i=0
while i < len(a):
    list1=a[i]
    j=0
    while j < len(a[i]):
        if list1[j]>0:
            b.append(list1[j])
        j+=1
    i+=1
for k in b:
     sum +=k
print sum
