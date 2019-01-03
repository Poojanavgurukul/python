user=input("enter a number\n")
if user>1:
    for i in range(2, user):
       if user%i==0:
           print(user, "is not a prime number")
	   break
    else:
       print(user, "is a prime number")
else:
    print(user, "is not a prime number")

