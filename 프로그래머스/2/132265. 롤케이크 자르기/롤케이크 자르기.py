from collections import Counter
def solution(topping):
    answer = 0
    dic1 = {}
    dic2 = Counter(topping)
    count = 0
    flag = False
    for i,val in enumerate(topping):
        dic2[val] -= 1
        if dic2[val] == 0:
            count += 1
        if dic1.get(val):
            dic1[val] += 1
        else:
            dic1[val] = 1
        if len(dic1) == len(dic2) - count:
            flag = True
            answer += 1
        if len(dic1) > len(dic2) - count:
            break
    print(sum(dic1.values()))
    return answer