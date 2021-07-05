# https://www.codewars.com/kata/5bb904724c47249b10000131/train/python


def points(games):
	count = 0
	for score in games:
		res = score.split(":")
		if res[0] > res[1]:
			count += 3
		elif res[0] == res[1]:
			count += 1
	return count

