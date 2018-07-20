'''
list A, N=len(A), triplet(P,Q,R), 0<=P<Q<R
@Find the maximal product of any triple@
N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].
'''

def solution(A):
	N=len(A)
	
	#當串列元素僅有三項 return積值
    if len(A)==3:
		return A[0]*A[1]*A[2]
	
	#串列排列 若不想改變串列A的值 可使用另一變數 ex:B = sorted(A)
	A.sort()
	
	#若最後一項元素值小於0 回傳最後三項乘積
	if A[N-1]<0:
		return A[N-3]*A[N-2]*A[N-1]
		
	#假設首項與二項皆為負數 並且與倒數二及三項比較乘積
	if A[0]*A[1] > A[N-3]*A[N-2]:
		return A[0]*A[1]*A[N-1]
	else:
		return A[N-3]*A[N-2]*A[N-1]
	
	pass
