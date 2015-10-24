def end_other(a, b):
	if len(a)>=len(b):
		A, B = a, b
	else:
		A, B = b, a
	if B.lower()==A[len(A)-len(B):].lower():  
		return True
	return False
