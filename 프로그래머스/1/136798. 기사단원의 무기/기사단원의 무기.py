import math
def solution(number, limit, power):
    answer = 0
    result = []
    for i in range(1,number+1):
        count = 0
        flag = True
        for j in range(1,int(math.sqrt(i))+1):
            if i % j == 0:
                if i == j*j:
                    count += 1
                else:
                    count += 2
            if count > limit:
                result.append(power)
                flag = False
                break
        if flag:
            result.append(count)
    answer = sum(result)
    return answer