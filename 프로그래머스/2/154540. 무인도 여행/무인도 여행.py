def solution(maps):
    answer = []
    visited = [[0 for i in range(len(maps[0]))] for j in range(len(maps))]
    
    def findfood(x,y):
        arr1 = [[x,y]]
        foods = int(maps[x][y])
        visited[x][y] = 1
        while arr1:
            x1,y1 = arr1.pop(0)
            for q,w in [[0,1],[0,-1],[1,0],[-1,0]]:
                if x1+q >= len(maps) or x1+q < 0 or y1+w >= len(maps[0]) or y1+w < 0:
                    continue
                if maps[x1+q][y1+w] != "X" and visited[x1+q][y1+w] == 0:
                    visited[x1+q][y1+w] = 1
                    foods += int(maps[x1+q][y1+w])
                    arr1.append([x1+q,y1+w])
        return foods
    
    for i,val1 in enumerate(maps):
        for j,val2 in enumerate(val1):
            if val2 != "X" and visited[i][j] == 0:
                answer.append(findfood(i,j))
    
    if not answer:
        answer.append(-1)
    
    answer.sort()
        
    return answer