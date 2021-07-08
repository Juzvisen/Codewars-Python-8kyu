# https://www.codewars.com/kata/57ab2d6072292dbf7c000039/python


def correct_polish_letters(s):
    return s.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))


