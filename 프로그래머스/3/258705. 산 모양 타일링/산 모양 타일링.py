def solution(n, tops):
    answer = 0
    arr1 = []
    if n==1:
        if tops[0] == 1: return 4
        else: return 3
    if n>1:
        if tops[0] == 1:
            arr1.append(4)
            arr1.append(arr1[0]*2)
            if tops[1] == 1:
                arr1[1] += arr1[0]
            arr1[1] += 3
        else:
            arr1.append(3)
            arr1.append(arr1[0]*2)
            if tops[1] == 1:
                arr1[1] += arr1[0]
            arr1[1] += 2
    for i in range(2,n):
        arr1.append((arr1[i-1]*2) + (arr1[i-1]-arr1[i-2]))
        if tops[i]:
            arr1[i] += arr1[i-1]
    return arr1[-1]%10007