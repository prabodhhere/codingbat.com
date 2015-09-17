def array_front9(nums):
	if len(nums)<4:
		l=len(nums)
	else:
		l=4
	for i in range(l):
		if nums[i]==9:
			return True
	return False
	