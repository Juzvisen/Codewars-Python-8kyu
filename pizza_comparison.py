# https://www.codewars.com/kata/5e2456b1c4d2810023bb14e2/python


def which_pizza(d1,price1,d2,price2):
	if d1**2 / price1 > d2**2 / price2:
		return d1
	return d2


