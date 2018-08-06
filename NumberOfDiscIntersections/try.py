#此code為錯誤答案

def solution(A):
    #半徑總和>圓心座標相減 相交
    #前項與後項比
    N=len(A)
    #圓數量為0,1 無相交
    if N<2:
        return 0;
    counter=0
    python={}
    for i in range(N):
        python[i]=A[i]
    rs_P= sorted(python.items(), key=operator.itemgetter(1),reverse=True)
    print(rs_P[0][0])
    for index in range(N):
        #ex:rs_P[0][0]=1,rs_P[0][1]=5 k will be 0 or 1 (rs_P[N][2])
        #判斷左側
        if rs_P[index][0]-rs_P[index][1]<0:
            counter+=rs_P[index][0]
            
        else:
            counter+=rs_P[index][1]
        #判斷右側
        if rs_P[index][0]+rs_P[index][1]>N-1:
            counter+=(N-1)-rs_P[index][0]
        else:
            counter+=rs_P[index][1]
        for j in range(index):
            if rs_P[index][0]-rs_P[index][1]<rs_P[j][0]<rs_P[index][0]+rs_P[index][1]:
                counter-=1
    return counter
    pass
