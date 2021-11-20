# https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/python


def distinct(seq):
    return sorted(set(seq), key = seq.index)