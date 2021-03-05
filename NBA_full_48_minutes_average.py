# https://www.codewars.com/kata/587c2d08bb65b5e8040004fd/python


def nba_extrap(ppg, mpg):
    return round(48 / mpg * ppg, 1) if mpg > 0 else 0


