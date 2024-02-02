def solution(number, k):
    answer = ''
    arr1 = [int(i) for i in number]
    arr2 = []
    for i in arr1:
        flag = False
        if not arr2 or k==0:
            arr2.append(i)
            continue
        while arr2:
            if arr2[-1] < i and k:
                arr2.pop()
                k -= 1
            else:
                arr2.append(i)
                flag = True
                break
        if not flag:
            arr2.append(i)
    for i in range(k):
        arr2.pop()
    for i in arr2:
        answer += str(i)
                
    return answer