def make_bricks(small, big, goal):
	if small>=goal:
		return True
	elif goal>(big*5 + small):
		return False
	elif ((goal/5)*5 + small) >= goal:
		return True
	else:
		return False	