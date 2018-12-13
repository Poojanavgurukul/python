#price_milk = raw_input("1L milk ka price daalo?")
#print "10L milk " + price_milk*10 + " rupees ka aata hai."
#out put of this 10L milk 12121212121212121212 rupees ka aata hai.
#it is multiply by ten times but we don't want that we wont to know the price so we have multipy that input user give
#TypeError: can't multiply sequence by non-int of type 'str'
#and we are taking string from the user not convert in integer.
#we can't add int and string
#price_milk = raw_input("1L milk ka price daalo?")
#print "10L milk " + price_milk*10 + " rupees ka aata hai."
price_milk = int(raw_input("1L milk ka price daalo?\n"))
print "10L milk " , price_milk*price_milk ," rupees ka aata hai."
