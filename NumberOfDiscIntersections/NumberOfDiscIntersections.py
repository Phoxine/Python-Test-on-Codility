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
        #圓心(first)座標+半徑 > 圓心(N-1)-圓心(first) 長度取後者
        if second-first>(N-1)-first:
            counter+=(N-1)-first
        else:
            counter+=second-first   
        for second in range(second+1,N):
            if second-first <= A[first]+A[second]:
                counter+=1;
            #相交次數大於1e7 回傳1
            if counter>10000000:
                return -1
        #print(first,counter)
    return counter
    pass