def max_end3(nums):
	l = max(nums[0], nums[2])
	for i in range(len(nums)):
		nums[i]=l
	return nums
