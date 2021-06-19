# https://www.codewars.com/kata/575fa9afee048b293e000287/python


def how_much_water(water,clothes,load):
	if load > 2 * clothes:
		return "Too much clothes"

	if load < clothes:
		return "Not enough clothes"

	for i in range(load - clothes):
		water *= 1.1

	return round(water, 2)


