def solution(n, computers):
    answer = n
    visited = [0 for i in range(n)]
    def DFS(x):
        nonlocal answer
        visited[x] = 1
        for i,val in enumerate(computers[x]):
            if val == 1 and visited[i] == 0:
                answer -= 1
                DFS(i)
    for i in range(n):
        if visited[i] == 0:
            DFS(i)
    return answer