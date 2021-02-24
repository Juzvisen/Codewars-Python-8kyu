# https://www.codewars.com/kata/55cb854deb36f11f130000e1/solutions/python


def weather_info(temperature):
    c = convert_to_celsius(temperature)
    if (c < 0):
        return f"{c} is freezing temperature"
    else:
        return f"{c} is above freezing temperature"


def convert_to_celsius(temperature):
    celsius = (temperature - 32) * (5 / 9)
    return celsius
 
