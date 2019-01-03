user=input()
i=0
if user>1:
    while i<user:
        if user%2==0:
           print user,"it not a prime"
           break
        i+=1 
        print user, "it is prime"
        break
else:
    print user,"it is not a prime" 
