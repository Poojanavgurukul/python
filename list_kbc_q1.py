question_list=["what is the caplital of india??","when we got independence??","who is the president of india??"]
option1_list=["A.delhi","A.26 jan 1950","A.narender modi"]
option2_list=["B.bangalore","B.14 aug 1947","B.rahul ghandi"]
option3_list=["C.bhopal","C.14aug 1948","C.pratibha patel"]
option4_list=["D.mumbai","D.14 jan 1959","D.dr. manmhoan singh"]
all_option=[option1_list,option2_list,option3_list,option4_list]
price_money=["1000","5000","10,000"]
ans_key=["a","b","c"]
counter = 0
while counter<len(question_list):
      print question_list[counter]
      print option1_list[counter]
      print option2_list[counter]
      print option3_list[counter]
      print option4_list[counter]
      user=raw_input("enter your answer\n")
      if user== ans_key[counter]:
	print "Congo you are correct."
	print price_money[counter]
      else:
	print "So, Sorry you lose the game"
	break
      counter=counter+1
