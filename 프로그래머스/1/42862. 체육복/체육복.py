def solution(n, lost, reserve):
    answer = 0
    arr1 = [1 for i in range(n)]
    for i in reserve:
        arr1[i-1] += 1
    
    for i in lost:
        arr1[i-1] -= 1
    
    
    arr1.insert(0,0)
    arr1.insert(n+1,0)
    print(arr1)
    for i in range(1,n+1):
        if arr1[i] == 0:
            if arr1[i-1] == 2:
                arr1[i-1] -= 1
                answer += 1
            elif arr1[i+1] == 2:
                arr1[i+1] -= 1
                answer += 1
        else:
            answer += 1
        
    return answer