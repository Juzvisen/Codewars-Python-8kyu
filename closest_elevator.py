# https://www.codewars.com/kata/5c374b346a5d0f77af500a5a


def elevator(left, right, call):
	if abs(call - left) < abs(call - right):
		return "left"
	else:
		return "right"

print(elevator(0,2,1))