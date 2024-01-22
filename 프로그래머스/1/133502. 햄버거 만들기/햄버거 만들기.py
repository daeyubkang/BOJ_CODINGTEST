def solution(ingredient):
    answer = 0
    a = ingredient
    length = len(ingredient)
    a.append(0)
    
    i = 0
    while i < length-3 and len(a) > 4:
        if a[i:i+4] == [1,2,3,1]:
            a.pop(i)
            a.pop(i)
            a.pop(i)
            a.pop(i)
            answer += 1
            i -= 3
        else:
            i += 1
    
    return answer