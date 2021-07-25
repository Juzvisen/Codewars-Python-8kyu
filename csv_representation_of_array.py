# https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036/python


def toCsvText(array):
    return '\n'.join(','.join(map(str, line)) for line in array)