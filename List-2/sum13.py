def sum13(nums):
	result=sum(nums)
	thirteen=[]
	thirteen = [i for i, x in enumerate(nums) if x%13==0]
	for i in range(len(thirteen)):
		if i!=len(thirteen)-1:	
			if thirteen[i]-thirteen[i+1]!=-1:
				result=result - nums[thirteen[i]] - nums[thirteen[i]+1]
			else:
				result=result - nums[thirteen[i]]
		else:
			if thirteen[i] == len(nums)-1:
				result=result - nums[len(nums)-1]
			else:
				result=result - nums[thirteen[i]] - nums[thirteen[i]+1]
	return result
