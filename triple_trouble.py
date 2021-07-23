# https://www.codewars.com/kata/5704aea738428f4d30000914/train/python


def triple_trouble(one, two,three):
	return "".join("".join(a) for a in zip(one, two,three))

