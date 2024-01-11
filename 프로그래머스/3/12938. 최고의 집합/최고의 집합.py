def solution(n, s):
    answer = []
    num1 = s//n
    num2 = s%n
    
    if s<n:
        return [-1]
    
    for i in range(n,0,-1):
        if(num2 >= i):
            answer.append(num1+1)    
            continue
            
        answer.append(num1)
    
    return answer