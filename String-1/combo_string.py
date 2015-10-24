def combo_string(a, b):
	if len(a)>len(b):
		long, short = a, b
	else:
		long, short = b, a
	return (short+long+short)