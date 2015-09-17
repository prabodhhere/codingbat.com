def last2(str):
	if len(str)<2:
		return 0
	toCompare=str[len(str)-2:]
	count=0
	for i in range(len(str)-2):
		if str[i:i+2]==toCompare:
			count+=1
	return count