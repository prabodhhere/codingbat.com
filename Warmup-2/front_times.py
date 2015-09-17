def front_times(str, n):
	if len(str)<3:
		s=str
	else:
		s=str[:3]
	r=''
	for i in range(n):
		r+=s
	return r

