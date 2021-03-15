# https://www.codewars.com/kata/55eea63119278d571d00006a/python


def next_id(arr):
    t = 0
    while t in arr:
        t += 1
    return t
