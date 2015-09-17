def array123(nums):
	a=[1, 2, 3]
	for i in range(len(nums)-2):
		if nums[i:i+3]==a:
			return True
	return False