example_dict = {"mom": "gordana", "mom-in-law": "gordana", "dad": "gojko",
"wife": "olga", "dad-in-law": "desha"}

def flip_dictionary(input_dict):
	new_dict = {}
	for key in input_dict:
		new_dict[input_dict[key]] = key
	return new_dict

print flip_dictionary(example_dict)