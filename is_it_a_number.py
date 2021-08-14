# https://www.codewars.com/kata/57126304cdbf63c6770012bd/python


def isDigit(string):
    try:
        float(string)
        return True
    except:
        return False