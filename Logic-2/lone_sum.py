def lone_sum(a, b, c):
	if a==b:
		if b==c:
			return 0
		else:
			return c
	if a==c:
		if c==b:
			return 0
		else:
			return b
	if b==c:
		if c==a:
			return 0
		else:
			return a
	return a+b+c
