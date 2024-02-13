def solution(board):
    answer = 0
    n = len(board)
    visited = [[[] for i in range(n)] for j in range(n)]
    def BFS(x,y):
        visited[0][0].append(0)
        arr1 = [[x,y,"f",0]]
        while arr1:
            x,y,d,s = arr1.pop(0)
            for q,w,e in [[0,1,"r"],[1,0,"d"],[0,-1,"l"],[-1,0,"u"]]:
                if x+q>=0 and y+w>=0 and x+q<n and y+w<n and board[x+q][y+w]==0:
                    if d == e:
                        m = 1
                    else:
                        m = 6
                    if not visited[x+q][y+w]:
                        visited[x+q][y+w].append(visited[x][y][s] + m)
                        arr1.append([x+q,y+w,e,len(visited[x+q][y+w])-1])
                    else:
                        if min(visited[x+q][y+w]) >= visited[x][y][s] + m - 3:
                            visited[x+q][y+w].append(visited[x][y][s] + m)
                            arr1.append([x+q,y+w,e,len(visited[x+q][y+w])-1])
    BFS(0,0)
    print(visited)
    return (min(visited[n-1][n-1])-5)*100