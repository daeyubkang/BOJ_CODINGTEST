def solution(grid):
    answer = []
    visited = [[[0,0,0,0] for i in range(len(grid[0]))] for i in range(len(grid))]
    node = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
    for i,val in enumerate(grid):
        for j,val2 in enumerate(val):
            node[i][j] = val2
    
    def findcycle(q,w,e):
        arr2 = [(q,w,e)]
        visited[q][w][e] = 1
        count = 0
        while arr2:
            x,y,z = arr2.pop()
            if count>0 and x==q and y==w and z==e: return count
            if (node[x][y] == "S" and z==0) or (node[x][y] == "L" and z==2) or (node[x][y] == "R" and z==3):
                if y==0:
                    arr2.append((x,len(grid[0])-1,0))
                    visited[x][len(grid[0])-1][0] = 1
                else:
                    arr2.append((x,y-1,0))
                    visited[x][y-1][0] = 1
            elif (node[x][y] == "S" and z==1) or (node[x][y] == "L" and z==3) or (node[x][y] == "R" and z==2):
                if y==len(grid[0])-1:
                    arr2.append((x,0,1))
                    visited[x][0][1] = 1
                else:
                    arr2.append((x,y+1,1))
                    visited[x][y+1][1] = 1
            elif (node[x][y] == "S" and z==2) or (node[x][y] == "L" and z==1) or (node[x][y] == "R" and z==0):
                if x==0:
                    arr2.append((len(grid)-1,y,2))
                    visited[len(grid)-1][y][2] = 1
                else:
                    arr2.append((x-1,y,2))
                    visited[x-1][y][2] = 1
            else:
                if x==len(grid)-1:
                    arr2.append((0,y,3))
                    visited[0][y][3] = 1
                else:
                    arr2.append((x+1,y,3))
                    visited[x+1][y][3] = 1
            count += 1
        return 1
            
    
    for i,val in enumerate(grid):
        for j,val2 in enumerate(val):
            for k in range(4):
                if not visited[i][j][k]:
                    answer.append(findcycle(i,j,k))
    
    if len(answer)>1: answer.sort()
    return answer