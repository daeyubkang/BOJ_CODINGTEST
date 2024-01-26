def solution(order):
    answer = 1
    arr1 = [i for i in range(order[0])]
    num1 = order[0] + 1
    dic1 = {order[0]: 1}
    
    for i in range(1, len(order)):
        if order[i] < arr1[-1]:
            break
        if order[i] == arr1[-1]:
            dic1[arr1.pop()] = 1
        elif order[i] == num1:
            num1 += 1
        elif order[i] > num1:
            arr1 += [i for i in range(num1,order[i])]
            num1 = order[i]+1
        answer = i + 1
    
    return answer