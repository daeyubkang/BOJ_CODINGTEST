def solution(players, callings):
    answer = players
    player  = {}
    
    for i,val in enumerate(players):
        player[val] = i
    

    
    for i,val in enumerate(callings):
        txt = player[val]
        txtVal = answer[txt-1]
        answer[txt] = txtVal
        answer[txt-1] = val
        player[val] -= 1
        player[txtVal] += 1
    
        
    return players