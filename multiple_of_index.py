# https://www.codewars.com/kata/5a34b80155519e1a00000009


def multiple_of_index(l):
	return [l[i] for i in range(1, len(l)) if l[i] % i == 0]


