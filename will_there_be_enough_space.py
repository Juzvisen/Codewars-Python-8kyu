def enough(cap, on, wait):
	return max(0, wait - (cap - on))

		
print(enough(100,50,50))