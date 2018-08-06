def solution(S):
    # write your code in Python 3.6
    #左右括號各設置一dict 並將同類型左右括號對應同一數字 list stack設為NULL
    left= { '(':1, '[':2, '{':3  }
    right={ ')':1, ']':2, '}':3  }
    stack=[]
    #以串列S首項為iteration做迴圈
    for character in S:
        #當character為 dict(left)的其中一項 push character對應的數字
        if character in left:
            stack.append(left[character])
        #當stack為空串列(if not x->x為false執行後面指令 true則否) 或是 左右括號dict對應的值不同 return 0   
        elif not len(stack) or right[character] != stack.pop():
            return 0
    #len(stack)為false return 1 ,true return 0        
    return 1 if not len(stack) else 0
    pass