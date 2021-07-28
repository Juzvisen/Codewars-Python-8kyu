# https://www.codewars.com/kata/5601409514fc93442500010b/train/python


def better_than_average(class_points, your_points):
	return sum(class_points, your_points) / (len(class_points) + 1) < your_points



