def create_password_generator(input_string):
	from random import choice

	def generate_password(password_length):
		output = ''
		for i in xrange(password_length):
			output += choice(input_string)
		return output
	return generate_password


alpha_password = create_password_generator('abcdef')
cartoon_password = create_password_generator('!@#$%%')

print alpha_password(5)
print alpha_password(10)
print cartoon_password(5) 
print cartoon_password(10) 