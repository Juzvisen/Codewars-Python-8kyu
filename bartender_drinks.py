# https://www.codewars.com/kata/568dc014440f03b13900001d/train/python

def get_drink_by_profession(param):
	if param.lower().title() == "Jabroni":
		return "Patron Tequila"
	elif param.lower().title() == "School Counselor":
		return "Anything with Alcohol"
	elif param.lower().title() == "Programmer":
		return "Hipster Craft Beer"
	elif param.lower().title() == "Bike Gang Member":
		return "Moonshine"
	elif param.lower().title() == "Politician":
		return "Your tax dollars"
	elif param.lower().title() == "Rapper":
		return "Cristal"
	else:
		return "Beer"
