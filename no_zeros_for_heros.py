# https://www.codewars.com/kata/570a6a46455d08ff8d001002/train/python


def no_boring_zeros(n):
	if n == 0:
		return 0
	else:
		return int(str(n).rstrip("0"))


