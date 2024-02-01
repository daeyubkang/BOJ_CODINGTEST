def solution(x, y, n):
    answer = 0
    arr1 = [1000003 for i in range(y+1)]
    arr1[x] = 0
    for i in range(x,y+1):
        if i+n <= y:
            arr1[i+n] = min(arr1[i+n], arr1[i]+1)
        if i*2 <= y:
            arr1[i*2] = min(arr1[i*2], arr1[i]+1)
        if i*3 <= y:
            arr1[i*3] = min(arr1[i*3], arr1[i]+1)
    
    if arr1[y] == 1000003:
        answer = -1
    else:
        answer = arr1[y]
    return answer