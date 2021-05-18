# https://www.codewars.com/kata/56f173a35b91399a05000cb7/python

def find_longest(strng):
    return max(len(a) for a in strng.split())
