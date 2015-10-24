def round10(s):
	if (s%10>=5 and s%10<=9):
		return s+10-(s%10)
	elif (s%10>=1 and s%10<=4):
		return (s-(s%10))
	else:
		return s
def round_sum(a, b, c):
	s=(round10(a)+round10(b)+round10(c))
	return s
