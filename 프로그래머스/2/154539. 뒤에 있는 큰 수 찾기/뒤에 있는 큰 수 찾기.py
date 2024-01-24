from collections import deque
def solution(numbers):
    mydeque = deque()
    answer = [-1 for i in range(len(numbers))]
    mydeque.append((numbers[0],0))
    for i in range(1,len(numbers)):
        while mydeque:
            if mydeque[-1][0] < numbers[i]:
                num1 = mydeque.pop()
                answer[num1[1]] = numbers[i]
            else:
                break
        mydeque.append((numbers[i],i))
    return answer