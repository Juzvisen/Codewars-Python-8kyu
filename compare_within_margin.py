# https://www.codewars.com/kata/56453a12fcee9a6c4700009c/python

def close_compare(a, b, margin = 0):
	return 0 if abs(a - b) <= margin else - 1 if b > a else 1
 
