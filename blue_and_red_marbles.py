# https://www.codewars.com/kata/5862f663b4e9d6f12b00003b/python


def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    blue_remaining = blue_start - blue_pulled
    red_remaining = red_start - red_pulled
    return blue_remaining / (blue_remaining + red_remaining)


