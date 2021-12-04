# https://www.codewars.com/kata/56a3f08aa9a6cc9b75000023/python


import re

def validate_usr(un):
	return re.match("^[a-z0-9_]{4,16}$",un) != None


