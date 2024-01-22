def solution(n, m, section):
    answer = 1
    num1 = section[-1] - m
    section.pop()
    num2 = 2
    while(len(section) > 0):
        if section[-1] <= num1:
            answer += 1
            num1 = section[-1] - m
            section.pop()
        else:
            section.pop()
        
    
    return answer