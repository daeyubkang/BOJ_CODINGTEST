def solution(n, roads, sources, destination):
    answer = []
    arr1 = [[] for i in range(n+1)]
    for i,j in roads:
        arr1[i].append(j)
        arr1[j].append(i)
    def BFS(x):
        visited[x] = 0
        arr2 = [[x,1]]
        while arr2:
            x, count = arr2.pop(0)
            for i in arr1[x]:
                if visited[i]==-1 or visited[i] > count:
                    visited[i] = count
                    arr2.append((i,count+1))
    visited = [-1 for i in range(n+1)]
    BFS(destination)
    for i in sources:
        answer.append(visited[i])
    return answer