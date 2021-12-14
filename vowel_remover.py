# https://www.codewars.com/kata/5547929140907378f9000039


def shortcut(s):
	for vowel in "aeoiu":
		s = s.replace(vowel,"")
	return s


