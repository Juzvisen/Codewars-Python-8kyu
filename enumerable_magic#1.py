# https://www.codewars.com/kata/54598d1fcbae2ae05200112c


def all(seq, fun):
    return next((False for x in seq if not fun(x)), True)