def quarter_of(month):
	if month in range(1, 4):
		return 1
	elif month in range(4, 7):
		return 2
	elif month in range(7, 10):
		return 3
	elif month in range(10, 13):
		return 4

print(quarter_of(1))
