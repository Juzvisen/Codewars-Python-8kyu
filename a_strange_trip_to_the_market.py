# https://www.codewars.com/kata/55ccdf1512938ce3ac000056/python


def is_lock_ness_monster(s):
    return any(i in s for i in ('tree fiddy', 'three fifty', '3.50'))
