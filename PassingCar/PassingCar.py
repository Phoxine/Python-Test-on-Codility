'''
list A, N=len(A)
@returns the number of pairs of passing cars.@
N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.
'''

'''
This Question is a little hard to understand it
let's see the example
A[0] = 0
A[1] = 1
A[2] = 0
A[3] = 1
A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

(P,Q)
P means the position that value is 0, Q means the position at A[P+1] to A[N-1] that value is 1.

011
01(0)11
2+(2+1)=5

in this question, we can count the passing car by reversed the list A

if list=[0,1,0,1,1]
A[4]=1	counter+=1	counter=1
A[3]=1  counter+=1	counter=2
A[2]=0	solution+=counter	counter=2,solution=2

A[1]=1  counter+=1	counter=3
A[0]=0  solution+=counter 	counter=3,solution=5

and solution is the answer. return it.
'''
def solution(A):
	N=len(A)
	
	#宣告變數counter,solution
	counter=0
	solution=0
	
	#從N-1項往回做迴圈運算 A[i]值為1 counter+=1 為0 將counter值加到solution
	for i in reversed(range(N))
		if A[i]==1
			counter+=1
		else:
			solution+=counter
	return solution
	
	pass
