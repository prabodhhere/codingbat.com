def xyz_there(str):
	if str[0:3]=='xyz':
		return True
	for i in range(len(str)-3):
		if str[i+1:i+4]=='xyz' and str[i]!='.':
			return True
	return False