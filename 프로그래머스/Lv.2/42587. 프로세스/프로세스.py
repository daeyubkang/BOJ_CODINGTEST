from collections import deque
def solution(priorities, location):
    deque1 = deque(priorities)
    arr1 = [0 for i in range(len(priorities))]
    answer = 0
    count = 1
    deque2= deque()
    for i in range(len(priorities)):
        deque2.append(i)
    while(arr1[location] == 0):
        if deque1[0] < max(deque1):
            deque1.append(deque1.popleft())
            deque2.append(deque2.popleft())
        else:
            deque1.popleft()
            arr1[deque2.popleft()] = count 
            count += 1
    
    return arr1[location]