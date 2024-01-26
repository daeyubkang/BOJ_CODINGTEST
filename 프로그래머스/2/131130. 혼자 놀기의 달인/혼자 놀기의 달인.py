def solution(cards):
    answer = 0
    arr1 = []
    arr2 = []
    visited = [0 for i in range(len(cards))]
    
    for i,val in enumerate(cards):
        if visited[val-1] > 0:
            continue
        count = 1
        arr1.append(val)
        visited[i] = 1
        while arr1:
            index1 = arr1.pop()
            if visited[index1-1] > 0:
                break
            visited[index1-1] = 1
            arr1.append(cards[index1-1])
            count += 1
        arr2.append(count)
    if len(arr2) == 1:
        return 0
    arr2.sort()
    answer = arr2[-1] * arr2[-2]
    return answer