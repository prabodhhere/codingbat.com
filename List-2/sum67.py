def sum67(nums):
	s=sum(nums)
	toS=0
	list=[]
	if len(nums)==0:
		return s
	for i in range(0, len(nums)-1):
		if nums[i]==6:
			if len(list)==0:
				list.append(i)
			elif list[-1]==7:
				list.append(i)
		if nums[i]==7 and nums[list[-1]]==6:
			list.append(i)
	if len(list)!=0:
		for i in range(0, len(list), 2):
			if i==len(list)-2:
				toS+=sum(nums[list[i]:list[-1]+1])	
			else:
				toS+=sum(nums[list[i]:list[i+2]])

	return (s-toS)