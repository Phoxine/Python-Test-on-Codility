'''
list A, N=len(A), (P,Q,E) 0<=P<Q<R<N
@returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.@
N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
'''

def solution(A):

	N=len(A)
	
	#list元素少於3 無法組成三角形 回傳0
	if N<3:
		return 0
	
	#排列 邊長不可為負 小於0值可忽略
	A.sort()
	
	for i in range(N-2):
		if A[i]>0 and A[i+1]>0 and A[i+2]>0:
			if A[i]+A[i+1]>A[i+2] and A[i]+A[i+2]>A[i+1] and A[i+1]+A[i+2]>A[i]:
            	return 1
        	else:
        	continue
        else:
        	continue
	
	#以上迴圈無回傳1 代表串列值無成三角形可能性 回傳0		
    return 0
    
    pass
