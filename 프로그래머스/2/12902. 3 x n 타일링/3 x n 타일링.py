def solution(n):
    answer = 0
    if n%2==1: 
        arr1 = [0]
    elif n==2: 
        arr1 = [3]
    elif n==4: 
        arr1 = [11]
    else:
        arr1 = [3,11]
        for i in range(2,n//2):
            result = (arr1[i-1]*4 - arr1[i-2]) % 1000000007
            arr1.append(result)
        
    return arr1[-1] 