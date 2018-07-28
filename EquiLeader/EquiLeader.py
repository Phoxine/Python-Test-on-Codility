#TimeComplexity = O(N*3) = O(N) 

def solution(A):
    candicate=0
    counter=0
    index=0
    #找leader
    #O(N)
    for i in range(len(A)):
        if counter==0:
            index=i
            candicate=A[i]
            counter+=1
        else:
            if A[i]==candicate:
                counter+=1
            else:
                counter-=1
    #先找串列中Leader數量 確認leader是否超過N一半以上
    #O(N)
    lnum=A.count(candicate)
    if lnum <= len(A)//2:
        return 0
    #將list A 含括leader分為兩部分 初始值為 [NULL] [ALL]
    answer=0    
    lcrt=0
    rcrt=lnum
    #O(N)
    for index,iterations in enumerate(A):
        if iterations==candicate:
            lcrt+=1
            rcrt-=1
        #左半部與右半部leader皆超過半數時,answer++
        if lcrt>(index+1)//2 and rcrt>(len(A)-1-index)//2 :
            answer+=1
    return answer
    pass