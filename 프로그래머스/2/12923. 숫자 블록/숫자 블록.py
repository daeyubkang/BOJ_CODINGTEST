import math
def solution(begin, end):
    answer = []
    for i in range(begin,end+1):
        if i==1: 
            answer.append(0)
            continue
        num1 = 1
        flag = False
        for j in range(2, int(math.sqrt(i))+1):
            if i%j==0:
                if i//j > 10000000:
                    num1 = j
                else:
                    answer.append(i//j)
                    flag = True
                    break
        if not flag:
            answer.append(num1)
                    
    return answer