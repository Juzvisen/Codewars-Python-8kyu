# https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python

def get_grade(s1,s2,s3):
	m = (s1 + s2 + s3) / 3.0
	if 90 <= m <= 100:
		return 'A'
	elif 80 <= m < 90:
		return 'B'
	elif 70 <= m < 80:
		return 'C'
	elif 60 <= m < 70:
		return 'D'
	return "F"


