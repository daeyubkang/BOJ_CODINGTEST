def solution(participant, completion):
    answer = ''
    dic1 = {}
    for i in participant:
        if dic1.get(i):
            dic1[i] += 1
            continue
        dic1[i] = 1
    for i in completion:
        dic1[i] -= 1
    for i in participant:
        if dic1[i] == 1:
            answer = i
            break
    return answer