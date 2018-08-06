def solution(H):
    #照順序擺放 當後項比前項小 pop前項 求append總次數 
    '''
    cr=0
    H[0] -> append   crt+=1                                     stack=[8]
    H[1] -> countinue                    cause H[0]=H[1]        stack=[8]
    H[2] -> append   crt+=1      H[0] -> pop cause H[2]<H[0]    stack=[5]
    H[3] -> append   crt+=1                                     stack=[5,7]
    H[4] -> append   crt+=1                                     stack=[5,7,9]
    H[5] -> append   crt+=1      H[4] -> pop cause H[5]<H[4]    stack=[5,7,8]
    H[6] -> countinue H[6]=H[3], H[5] -> pop cause H[6]<H[5]    stack=[5,7,]
    H[7] -> append   crt+=1      H[2] -> pop cause H[7]<H[2]    stack=[4]
    H[8] -> append   crt+=1                                     stack=[4,8]
    crt=7
    '''
    stack=[]
    counter=0
    for height in H:
        while stack and stack[-1]>height:
            stack.pop()
        if stack and stack[-1]==height:
            continue
        else:
            counter+=1
            stack.append(height)
        #print(height,stack)
    return counter
    pass