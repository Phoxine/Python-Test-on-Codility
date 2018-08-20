'''
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:

A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0
the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
Assume that:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
'''

def solution(A):
	# write your code in Python 3.6
	#if list A is NULL 
	if len(A)==0:
		return 0
	temp=0
	Max_Slice=-1000000
	#若list A元素全為負數 最後將回傳Negative_Max
	Negative_Max=-1000000
	for i in range(len(A)):
		if A[i]>=0:
			temp+=A[i]
			Max_Slice=max(temp,Max_Slice)
		else:
			#example: [3,4,-6,100] 最大值為4數之和 -> 3 + 4 + (-6) + 100 = 101
			if temp + A[i]>0:
				temp+=A[i]
				Negative_Max=max(Negative_Max, A[i])
			else:
				#不符合上述條件，將暫存值歸零
				temp=0 
				Negative_Max=max(Negative_Max,A[i])
				
	#list A其中一元素>=0 回傳Max_Slice, 否則回傳Negative_Max
	return Max_Slice if Max_Slice!=-1000000 else Negative_Max
	pass
