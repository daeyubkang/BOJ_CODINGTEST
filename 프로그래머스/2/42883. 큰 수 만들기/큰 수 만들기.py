def solution(number, k):
    answer = ''
    arr1 = [int(i) for i in number]
    arr2 = []
    for i in arr1:
        while arr2 and k:
            if arr2[-1] < i and k:
                arr2.pop()
                k -= 1
            else:
                break
        arr2.append(i)
    for i in range(k):
        arr2.pop()
    for i in arr2:
        answer += str(i)
                
    return answer