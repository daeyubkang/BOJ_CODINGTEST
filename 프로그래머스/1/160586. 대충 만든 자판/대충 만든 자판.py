def solution(keymap, targets):
    answer = []
    mydic = {}
    for i,val in enumerate(keymap):
        for j,val2 in enumerate(list(val)):
            if(mydic.get(val2)):
                mydic[val2] = min(mydic[val2],j+1)
            else:
                mydic[val2] = j+1
                
    for i,val in enumerate(targets):
        result = 0
        flag = True
        for j,val2 in enumerate(list(val)):
            if(mydic.get(val2)):
                result += mydic[val2]
            else:
                answer.append(-1)
                flag = False
                break
        if(flag):
            answer.append(result)
    return answer