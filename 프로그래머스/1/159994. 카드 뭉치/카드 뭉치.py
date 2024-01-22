from collections import deque
def solution(cards1, cards2, goal):
    answer = 'Yes'
    deque1 = deque(cards1)
    deque2 = deque(cards2)
    
    print(deque1,deque2)
    
    for i in goal:
        flag = False
        if len(deque1) > 0:
            if i == deque1[0]:
                deque1.popleft()
                flag = True
        if len(deque2) > 0:
            if i == deque2[0]:
                deque2.popleft()
                flag = True
        if(not flag):
            return 'No'
            
    
    return answer