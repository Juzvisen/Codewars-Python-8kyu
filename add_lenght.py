#https://www.codewars.com/kata/559d2284b5bb6799e9000047/python

def add_length(str_):
    return [f'{x} {len(x)}' for x in str_.split()]


print(add_length('apple ban'))


