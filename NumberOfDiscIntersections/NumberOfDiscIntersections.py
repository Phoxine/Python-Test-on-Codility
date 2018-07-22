def solution(A):
    #半徑總和>圓心座標相減 相交
    #前項與後項比
    N=len(A)
    counter=0
    #圓數量為0,1 無相交
    if N<2:
        return 0;
    for first in range(N-1):
        second=first+A[first]
        counter+=A[first]
        for second in range(first+1,N):

            if second-first <= A[first]+A[second]:
                counter+=1;
    #相交次數大於1e7 回傳1
    if counter>10000000:
                    return -1            
    return counter
    pass