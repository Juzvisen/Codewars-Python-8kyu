# https://www.codewars.com/kata/57f222ce69e09c3630000212/train/python


def well(x):
	c = x.count("good")
	return "I smell a series!" if c > 2 else "Publish!" if c else "Fail!"


