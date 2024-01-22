def solution(s):
    answer = []
    result = {}
    
    for i, val in enumerate(list(s)):
        if (result.get(val) != None):
            answer.append(i-result[val])
            result[val] = i
        else:
            result[val] = i
            answer.append(-1)
    print(result)
    return answer