# https://www.codewars.com/kata/5dd462a573ee6d0014ce715b


def same_case(a,b):
	if a.islower() and b.islower():
		return 1
	elif a.isupper() and b.isupper():
		return 1
	elif not a.isalpha() or not b.isalpha():
		return -1
	else:
		return 0

