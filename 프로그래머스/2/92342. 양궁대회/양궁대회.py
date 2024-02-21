from itertools import product
def solution(n, info):
    answer = []
    sumval1 = 0
    for i,val in enumerate(info):
        if val>0:
            sumval1 += 10-i
    array_length = 10
    boolean_combinations = list(product([True, False], repeat=array_length))
    point = 1
    for combination in boolean_combinations:
        result = [0 for q in range(11)]
        target = sumval1
        target2 = 0
        n1 = n
        for i,val in enumerate(combination):
            if not val:
                continue
            else:
                if info[i]+1<=n1:
                    n1 -= info[i]+1
                    if info[i] > 0:
                        target -= 10-i
                    target2 += 10-i
                    result[i] = info[i]+1
        if n1>0:
            result[10] = n1
        if target2-target > point:
            answer = result
            point = target2-target
        elif target2-target == point:
            if answer and answer == result:
                continue
            elif answer:
                for w in range(11):
                    if answer[10-w] < result[10-w]:
                        answer = result
                        break
                    elif answer[10-w] > result[10-w]:
                        break
    if not answer:
        answer.append(-1)
    return answer