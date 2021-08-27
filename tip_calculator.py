# https://www.codewars.com/kata/56598d8076ee7a0759000087/python


from math import ceil
def calculate_tip(amount, rating):
    tips = {
        'terrible': 0,
        'poor' : .05,
        'good' : .1,
        'great' : .15,
        'excellent' : .2
    }
    if rating.lower() in tips:
        return ceil(amount * tips[rating.lower()])
    else:
        return 'Rating not recognised'

