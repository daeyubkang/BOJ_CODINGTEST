def solution(n, wires):
    answer = -1
    arr1 = [[] for i in range(n+1)]
    result = []
    def DFS(x):
        nonlocal count
        for i in arr1[x]:
            if visited[i] == 0:
                count += 1
                visited[i] = 1
                DFS(i)
    
    for x,y in wires:
        arr1[x].append(y)
        arr1[y].append(x)

    print(arr1)
    for i in wires:
        num1 = i[0]
        num2 = i[1]
        visited = [0 for i in range(n+1)]
        arr1[num2].remove(num1)
        arr1[num1].remove(num2)
        count = 1
        visited[num1] = 1
        DFS(num1)
        arr1[num1].append(num2)
        arr1[num2].append(num1)
        result.append(abs((n-count)-count))
        
    result.sort()
    print(result)
    answer = result[0]
    
    return answer