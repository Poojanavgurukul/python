students=int(raw_input("enter number of student\n"))
money_spend_student=int(raw_input("enter money spend on student\n"))
total_spended_money=students*money_spend_student
if total_spended_money<50000:
	print total_spended_money,"hum budget ke ander hai"
else:
	print total_spended_money,"budget ke bahar hai"
