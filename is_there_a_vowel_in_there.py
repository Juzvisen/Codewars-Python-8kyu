# https://www.codewars.com/kata/57cff961eca260b71900008f/python


def is_vow(inp):
    return [chr(n) if chr(n) in "aeiou" else n for n in inp]


