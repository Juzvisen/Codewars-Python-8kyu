# https://www.codewars.com/kata/57e92e91b63b6cbac20001e5/python


def duty_free(price, discount, holiday_cost):
	saving = price * discount / 100.0
	return int(holiday_cost / saving)


