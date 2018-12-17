#xdef numbers_greater_than_twenty(list):
  #counter = 0
  #while counter < len(list):
    #item = list[counter]
   # if item > 20:
  #    list.remove(item)
 # return list

#num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

#num_list_20 = numbers_greater_than_twenty(num_list)

#print "Initial list", num_list
#print "List that doesn't contain numbers greate than 20", new_list

def numbers_greater_than_twenty(list):
  counter = 0
  list_20=[]
  while counter < len(list):
    item = list[counter]
    if item < 20: 
	list_20.append(item) 
    counter=counter+1
  return list_20

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
new_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

num_list_20 = numbers_greater_than_twenty(new_list)

print "Initial list", num_list
print "List that doesn't contain numbers greate than 20", num_list_20

