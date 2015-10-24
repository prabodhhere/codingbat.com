def rotate_left3(nums):
	result=[]
	result.extend(nums[1:])
	result.append(nums[0])
	return result

rotate_left3([1, 2, 3])
