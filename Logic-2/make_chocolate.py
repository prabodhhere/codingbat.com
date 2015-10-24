def make_chocolate(small, big, goal):
	r=goal-big*5
	if goal>=big*5:
		if r>=0 and r<=small:
			r = goal-big*5
		else:
			r=-1
	else:
		if (goal-(goal/5)*5)<=small:
			r=goal-(goal/5)*5
		else:
			r=-1
	return r