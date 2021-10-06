# https://www.codewars.com/kata/5761a717780f8950ce001473/train/python


def calculate_age(year_of_birth, current_year):
	sum = current_year - year_of_birth
	

	if sum == 1:
		return f"You are 1 year old."
	elif sum == -1:
		return f"You will be born in 1 year."
	if sum > 0:
		return f"You are {sum} years old."
	elif sum < 0:
		return f"You will be born in {sum * -1} years."
	elif sum == 0:
		return f"You were born this very year!" 
	


