def solution(t, p):
    answer = 0
    
    length = len(list(p))
    print(length)
    
    for i in range(0,len(list(t))-length+1):
        if int(t[i:length+i]) <= int(p):
            answer += 1
    
    return answer