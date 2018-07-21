'''
list A, N=len(A),0 ≤ P < Q < N
@The goal is to find the starting position of a slice whose average is minimal.@
N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
---------------------------------
For example, array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:
slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
----------------------------------
'''
def solution(A):

	#solution用來與計算出來的平均值比較 answer則是將元素項次記錄
	N=len(A)
	solution = 10001
	answer=0
	
	#第一個迴圈跑A[0]-A[N-2], 第二個迴圈則是從A[START+1]-A[N-1]
	#length代表slice長度 avg 初始值設為list A首項
	for START in range(0,N-1):
		length=1
		avg=A[START]
		for END in range(START+1,N):
			if length>1 and A[END]>=avg:
				break
			length+=1
			avg = (avg*(length-1)+A[END])/length
            
		if avg<solution:
			solution = avg
			answer=START
    return answer
    pass
