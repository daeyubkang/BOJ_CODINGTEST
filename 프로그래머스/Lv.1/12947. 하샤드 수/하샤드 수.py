def solution(x):
    answer = True
    
    arr1 = list(str(x))
    sum = 0
    for i in arr1:
        sum += int(i)
    
    if x%sum == 0:
        answer = True
    else:
        answer = False
    
    return answer