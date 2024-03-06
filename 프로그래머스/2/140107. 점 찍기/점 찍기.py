import math
def solution(k, d):
    answer = (d//k) + 1
    for i in range(k,d+1,k):
        answer += (math.floor(math.sqrt(d**2-i**2))//k)+1
    return answer