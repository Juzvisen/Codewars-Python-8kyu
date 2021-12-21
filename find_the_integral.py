# https://www.codewars.com/kata/59811fd8a070625d4c000013/python


def integrate(coef, exp):
    exp = exp + 1
    coef = coef / exp if coef % exp else coef // exp
    return f"{coef}x^{exp}"