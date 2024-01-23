from collections import deque
def solution(food):
    answer = ''
    arr1 = []
    mydeque = deque([0])
    for i,val in enumerate(food):
        if i == 0:
            continue
        if val//2 > 0:
            arr1.append([i for j in range(val//2)])
    
        
    arr2 = sorted(arr1,reverse=True)
    
    arr1 += [[0]] + arr2
    
    print(arr1)
    
    for i,val in enumerate(arr1):
        for j in val:
            answer += str(j)
    
    return answer