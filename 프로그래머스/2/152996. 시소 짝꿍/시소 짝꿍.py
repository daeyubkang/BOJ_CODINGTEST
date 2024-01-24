from collections import Counter
def solution(weights):
    answer = 0
    dic1 = Counter(weights)
    
    setweights = sorted(set(weights))
    
    for i in setweights:
        for j in [1,2,3/2,4/3]:
            if dic1.get(i*j):
                if j == 1:
                    answer += dic1[i*j] * (dic1[i*j]-1) / 2
                else:
                    answer += dic1[i*j] * dic1[i]
            
    return answer