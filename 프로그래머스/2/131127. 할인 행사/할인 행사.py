from collections import Counter
def solution(want, number, discount):
    answer = 0
    for i,val in enumerate(discount):
        flag = True
        if i > len(discount)-10:
            arr1 = discount[i:]
        else:
            arr1 = discount[i:i+10]
        for j,val2 in enumerate(want):
            if Counter(arr1).get(val2) != None and Counter(arr1).get(val2) >= number[j]:
                continue
            else:
                flag = False
                break
        if flag: answer += 1 
    return answer