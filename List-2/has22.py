def has22(nums):
	for i in xrange(len(nums)):
		if nums[i]==2 and (i!=len(nums)-1 and nums[i+1]==2):
			return True
	return False