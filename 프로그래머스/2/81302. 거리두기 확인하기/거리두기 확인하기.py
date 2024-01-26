def solution(places):
    answer = []
    copyarr = [[[0 for i in range(len(places[0][0])+4)] for j in range(len(places[0])+4)] for k in range(len(places))]
    for i,val1 in enumerate(places):
        for j,val2 in enumerate(val1):
            for k,val3 in enumerate(val2):
                if val3 == "P":
                    copyarr[i][j+2][k+2] = 1
                elif val3 == "X":
                    copyarr[i][j+2][k+2] = 2
    
    for i,val1 in enumerate(places):
        flag = True
        for j,val2 in enumerate(val1):
            for k,val3 in enumerate(val2):
                if val3 == "P":
                    copyarr[i][j+2][k+2]
                    for q,w in [[1,0],[-1,0],[0,1],[0,-1]]:
                        if copyarr[i][j+2+q][k+2+w] == 1:
                            flag = False
                            break
                    if not flag: break
                    
                    for q,w in [[1,1],[-1,-1],[-1,1],[1,-1]]:
                        if copyarr[i][j+2+q][k+2+w] == 1 and (copyarr[i][j+2+q][k+2] != 2 or copyarr[i][j+2][k+2+w] != 2):
                            flag = False
                            break
                    if not flag: break
                    
                    for q,w in [[2,0],[-2,0],[0,2],[0,-2]]:
                        if copyarr[i][j+2+q][k+2+w] == 1 and copyarr[i][j+2+q//2][k+2+w//2] != 2:
                            flag = False
                            break
                    if not flag: break
            if not flag: break
            
        if not flag:
            answer.append(0)
        else:
            answer.append(1)
    return answer