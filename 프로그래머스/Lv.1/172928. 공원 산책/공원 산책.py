def solution(park, routes):
    answer = []
    q,w = 0,0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                q,w = i,j         
                break
                
    print(q,w)
    
    for j in routes:
        direction = j.split(" ")[0]
        num1 = int(j.split(" ")[1])
        flag = True
        
        if direction == "E":
            if w+num1 > len(park[0])-1:
                continue
            for i in range(1,num1+1):
                if(park[q][w+i]=="X"):
                    flag = False
                    break
            if flag:
                w += num1
            
        elif direction == "W":
            if w-num1 < 0:
                continue
            for i in range(1,num1+1):
                if(park[q][w-i]=="X"):
                    flag = False
                    break
            if flag:
                w -= num1
        elif direction == "S":
            if q+num1 > len(park)-1:
                continue
            for i in range(1,num1+1):
                if(park[q+i][w]=="X"):
                    flag = False
                    break
            if flag:
                q += num1
        else:
            if q-num1 < 0:
                continue
            for i in range(1,num1+1):
                if(park[q-i][w]=="X"):
                    flag = False
                    break
            if flag:
                q -= num1
    
    return [q,w]