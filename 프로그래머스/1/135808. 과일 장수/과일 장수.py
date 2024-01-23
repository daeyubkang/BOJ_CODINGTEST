def solution(k, m, score):
    answer = 0
    sortarr = sorted(score,reverse=True)
    
    i = 0
    count = 0
    for i in range(len(score)//m):
        if sortarr[i] > k:
            continue
        answer += min(sortarr[i*m:i*m+m]) * m
    
    return answer