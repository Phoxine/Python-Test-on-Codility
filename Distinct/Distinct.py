'''
list A, N=len(A)
@return the number of distinct values in array A.
N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''
def solution(A):
	N=len(A
	#若為串列為空 回傳0
	if N==0;
		return 0
	
	#串列排列 亦可用 sorted(A)
	A.sort()
	
	#計數器變數宣告
	counter=1
	
	#串列A[0]-A[N-1] i項與i+1項相等 則做下一個迴圈  否則counter值+1
	for i in range(N-1):
		if A[i+1]==A[i]:
			continue
		else:
			counter+=1
	
	return counter
	
	pass

	##hello world
