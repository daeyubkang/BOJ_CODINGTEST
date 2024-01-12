def solution(board, h, w):
    answer = 0
    board2 = [[0 for _ in range(len(board)+2)] for _ in range(len(board)+2)]
    
    for i in range(len(board)):
        for j in range(len(board)):
            board2[i+1][j+1] = board[i][j]    
    
    xy = [[-1,0],[+1,0],[0,-1],[0,+1]]
    
    for x,y in xy:
        if board2[h+x+1][w+y+1] == board[h][w]:
            answer += 1
    
    # arr1 = [board[h-1][w],board[h-1][w],board[h-1][w],board[h-1][w]]
        
    
    return answer