def prefix_calc():
	operator = raw_input(str("Please enter a math operator: "))
	first_number = raw_input("Please enter an integer: ")
	second_number = raw_input("Please enter another integer: ")
	if operator == '+':
		print int(first_number) + int(second_number)
	elif operator == '-':
		print int(first_number) - int(second_number)
	elif operator == '/':
		print int(first_number) / int(second_number)
	elif operator == '*':
		print int(first_number) * int(second_number)
	elif operator == '**':
		print int(first_number) ** (second_number)
	else:
		print "Not a valid mathematical operator."

prefix_calc()