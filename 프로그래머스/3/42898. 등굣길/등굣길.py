def solution(m, n, puddles):
    answer = 0
    visited = [[0 for i in range(m)] for j in range(n)]
    for i,j in puddles:
        visited[j-1][i-1] = -1
    visited[0][0] = 1
        
    for i in range(n):
        for j in range(m):
            if visited[i][j] == -1: continue
            for q,w in [[0,1],[1,0]]:
                if i-q>=0 and j-w>=0 and visited[i-q][j-w] != -1:
                    visited[i][j] += visited[i-q][j-w]
    answer = visited[n-1][m-1]
    return answer%1000000007