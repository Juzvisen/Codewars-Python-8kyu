# https://www.codewars.com/kata/59c8b38423dacc7d95000008/python


def isValid(formula):
    if 1 in formula and 2 in formula: return False
    if 3 in formula and 4 in formula: return False
    if 5 in formula and 6 not in formula: return False
    if 5 not in formula and 6 in formula: return False
    if 7 not in formula and 8 not in formula: return False
    return True


