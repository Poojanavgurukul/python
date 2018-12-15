marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]

counter1=0
while counter1<len(marks):
	small_list_length = len(marks[counter1])
	print max(marks[counter1])
	counter1=counter1+1
