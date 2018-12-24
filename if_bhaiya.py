max=30
min=5
av=15
user=input("enter a number\n")
if user<=max and user>=av:
     print "A","close to max"
elif user<=av and user>min:
     print "B","close to average"
elif user<=min:
     print "C","close to min"
else:
     print "D","more than max"

