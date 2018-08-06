def solution(A, B):
    # write your code in Python 3.6
    N=len(A)
    #設置一空堆疊(串列)
    stack=[]
    for i in range(N):
        #魚大小
        size = A[i]
        #魚游向
        direction = B[i]
        #當堆疊為空 push第i條魚
        if not stack:
            stack.append(i)
        else:
            #堆疊非empty 且 當前第i條魚游向上游,堆疊最上面一條魚游向下游 且 第i條魚較大
            while  stack and direction - B[stack[-1]] == -1 and A[stack[-1]] < size:
                stack.pop()
            #第i條魚放入堆疊的情況
            if  stack:
                if direction - B[stack[-1]] != -1:
                    stack.append(i)
            else:
                stack.append(i)
    #最後return堆疊總數     
    return len(stack)
    pass