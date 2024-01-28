def solution(queue1, queue2):
    answer = -2
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    if (sum1+sum2)%2 == 1: return -1
    arr1 = queue1 + queue2 + [0]
    sumvalue = (sum1+sum2)//2
    point1 = 0
    point2 = len(queue1) - 1
    result = []
    while point2 < len(queue1)*2 and point1 <= point2:
        if sum1 < sumvalue:
            point2 += 1
            sum1 += arr1[point2]
        elif sum1 > sumvalue:
            sum1 -= arr1[point1]
            point1 += 1
        if sum1 == sumvalue:
            result.append((point1,point2))
            point2 += 1
            sum1 += arr1[point2] - arr1[point1]
            point1 += 1
        
    if not result:
        return -1

    if result[0][1] == len(queue1) - 1:
        answer = result[0][0]
    elif result[0][0] == 0:
        answer = (result[0][1] - (len(queue1)-1))
    else:
        answer = (result[0][0] - 0) + (result[0][1] - (len(queue1) - 1))
    
    for i in range(1,len(result)):
        if result[i][1] == len(queue1) - 1:
            value = result[i][0]
        elif result[i][0] == 0:
            value = (result[i][1] - (len(queue1)-1))
        else:
            value = result[i][0] - 0 + result[0][1] - (len(queue1) - 1)
        answer = min(answer,value)

    return answer