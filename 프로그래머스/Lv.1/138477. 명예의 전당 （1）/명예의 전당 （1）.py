def solution(k, score):
    answer = []
    arr1 = [2001 for i in range(k)]
    for i in range(len(score)):
        
        arr1.append(score[i])
        arr1.sort(reverse=True)
        if k > i:
            del arr1[0]
            answer.append(arr1[-1])
            continue
        del arr1[-1]
        answer.append(arr1[-1])
        
    return answer