#refer to https://stackoverflow.com/questions/4801242/algorithm-to-calculate-number-of-intersecting-discs/26138026#26138026

from bisect import bisect_right

def solution(A):
    #半徑總和>圓心座標相減 相交
    #前項與後項比
    N=len(A)
    result=0
    #圓數量為0,1 無相交
    if N<2:
        return 0;
    counter=0
    #直接排列成圓範圍
    CR= sorted( [(i-A[i], i+A[i]) for i in range(len(A))] )
    #CR[i][0]所有項設為另一list 給予length
    start = [i[0] for i in CR]
    #比較左側、右側
    for i in range(N):
        end   = CR[i][1]
        #bisect_right(start,end) == all(val <= end for val in start[0:i]) for leftside
        #all(val > end for val in start[i:N]) for right
        count = bisect_right(start,end)
        count-=(i+1)
        result+=count
        if result>1e7:
            return -1
    return result
    pass
