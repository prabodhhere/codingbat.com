def fix_teen(n):
	if n==13 or n==14 or n==17 or n==18 or n==19:
		return True
	else:
		return False
def no_teen_sum(a, b, c):
	s=0
	if fix_teen(a)==False:
		s+=a
	if fix_teen(b)==False:
		s+=b
	if fix_teen(c)==False:
		s+=c
	return s