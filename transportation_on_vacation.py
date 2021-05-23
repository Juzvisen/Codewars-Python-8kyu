# https://www.codewars.com/kata/568d0dd208ee69389d000016/train/python


def rental_car_cost(d):
	price = d * 40
	if d >= 7:
		 price -= 50
	elif d >= 3:
		 price -= 20
	return price
	

print(rental_car_cost(7))




