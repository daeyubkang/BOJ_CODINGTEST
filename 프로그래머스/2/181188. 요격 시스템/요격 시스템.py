def solution(targets):
    answer = 1
    targets.sort()
    end = targets[0][1]
    for i in range(1, len(targets)):
        if targets[i][0] >= end:
            answer += 1
            end = targets[i][1]
        else:
            if targets[i][1] < end:
                end = targets[i][1]
        
    return answer