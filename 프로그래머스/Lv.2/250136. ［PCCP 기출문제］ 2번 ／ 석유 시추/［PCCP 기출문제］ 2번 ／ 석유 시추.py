from collections import deque
def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    visited = [[0 for i in range(m)] for j in range(n)]
    result = [0 for i in range(m)]
    xy = [[0,1],[0,-1],[1,0],[-1,0]]
    
    def BFS(x,y):
        q = deque()
        q.append([x,y])
        count = 1
        max_y = y
        min_y = y
        visited[x][y] = 1
        
        while(q):
            x1,y1 = q.popleft()
            max_y = max(max_y, y1)
            min_y = min(min_y, y1)
            for nx,ny in xy:
                nx += x1
                ny += y1
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if land[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append([nx,ny])
                    visited[nx][ny] = 1
                    count += 1
        for i in range(min_y,max_y+1):
            result[i] += count
        
    for i in range(n):
        for j in range(m):
            if(land[i][j] == 1 and visited[i][j] == 0):
                BFS(i,j)
            
    answer = max(result)
    return answer