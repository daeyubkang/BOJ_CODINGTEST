def solution(board):
    answer = 0
    arr1 = [["D" for i in range(len(board[0])+2)] for j in range(len(board)+2)]
    visited = [[len(board)*len(board[0]) for i in range(len(board[0])+2)] for j in range(len(board)+2)]
    startX, startY = 0,0
    for i in range(len(board)):
        for j in range(len(board[0])):
            arr1[i+1][j+1] = board[i][j]
            if board[i][j] == "R":
                startX, startY = i+1,j+1
            
    def BFS(x,y):
        arr2 = [[x,y]]
        visited[x][y] = 0
        while arr2:
            q,w = arr2.pop(0)
            for q1,w1 in [[0,1],[0,-1],[1,0],[-1,0]]:
                count = 1
                while count < 100:
                    if arr1[q+(q1*count)][w+(w1*count)] == "D":
                        if count == 1:
                            break
                        q2,w2 = q+(q1*(count-1)), w+(w1*(count-1))
                        if arr1[q2][w2] == "G":
                            return visited[q][w] + 1
                        if visited[q2][w2] > visited[q][w] + 1:
                            visited[q2][w2] = visited[q][w] + 1
                            arr2.append([q2,w2])
                        break
                    count += 1
                
        return -1
    
    answer = BFS(startX,startY)
    return answer