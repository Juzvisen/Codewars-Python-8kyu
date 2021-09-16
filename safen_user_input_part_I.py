# https://www.codewars.com/kata/56bcaedfcf6b7f2125001118/python


def html_special_chars(data):
	symbols = {'<': '&lt;', '>': '&gt;', '"': '&quot;', '&': '&amp;'}
	return "".join(symbols.get(x, x) for x in data)


