# https://www.codewars.com/kata/56f6919a6b88de18ff000b36/train/python

def how_many_dalmatians(n):
	dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];

	return dogs[0] if n <= 10 else dogs[1] if n <=50 else dogs[3] if n == 101 else dogs[2]


