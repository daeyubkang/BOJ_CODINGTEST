def solution(maps):
    def findXY(x,y,goal):
        visited = [[0 for i in range(len(maps[0]))] for j in range(len(maps))]  
        visited[x][y] = 1
        memory = [[x,y]]
        while memory:
            qw = memory.pop(0)
            q = qw[0]
            w = qw[1]
            for i,j in [[-1,0],[1,0],[0,-1],[0,1]]:
                if q + i >= len(maps) or q + i < 0 or w + j >= len(maps[0]) or w + j < 0:
                    continue
                if maps[q+i][w+j] == "X" or visited[q+i][w+j] != 0:
                    continue
                if maps[q+i][w+j] == goal:
                    return visited[q][w] + 1
                memory.append([q+i,w+j])
                visited[q+i][w+j] = visited[q][w] + 1
        return -1
    
    answer = 0
    start = []
    middle = []
    for i,val in enumerate(maps):
        if val.find("S") >= 0:
            start = [i,val.find("S")]
        if val.find("L") >= 0:
            middle = [i,val.find("L")]
    middleResult = findXY(start[0],start[1],"L")
    if middleResult == -1:
        return -1
    answer += middleResult
    result = findXY(middle[0],middle[1],"E")
    if result == -1:
        return -1
    answer += result-2
    
    
    return answer