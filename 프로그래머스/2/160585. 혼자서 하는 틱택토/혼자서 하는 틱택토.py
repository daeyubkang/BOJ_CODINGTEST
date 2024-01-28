def solution(board):
    answer = 1
    num1 = 0
    num2 = 0
    arr1 = []
    dic1 = {}
    arr2 = []
    dic2 = {}
    for i,val1 in enumerate(board):
        for j,val2 in enumerate(val1):
            if val2 == "O":
                num1 += 1
                dic1[i,j] = 1
                arr1.append((i,j))
            elif val2 == "X":
                num2 += 1
                dic2[i,j] = 1
                arr2.append((i,j))
                
    if num1 < num2 or num1-1 > num2:
        return 0
    
    if num1 == num2:
        for i,val in enumerate(arr1):
            if val[0] == 0:
                if dic1.get((1,val[1])) != None and dic1.get((2,val[1])) != None:
                    return 0
            if val[1] == 0:
                if dic1.get((val[0],1)) != None and dic1.get((val[0],2)) != None:
                    return 0
            if val[0] == 0 and val[1] == 0:
                if dic1.get((1,1)) != None and dic1.get((2,2)) != None:
                    return 0
            if val[0] == 0 and val[1] == 2:
                if dic1.get((1,1)) != None and dic1.get((2,0)) != None:
                    return 0
                
    if num1-1 == num2:
        for i,val in enumerate(arr2):
            if val[0] == 0:
                if dic2.get((1,val[1])) != None and dic2.get((2,val[1])) != None:
                    return 0
            if val[1] == 0:
                if dic2.get((val[0],1)) != None and dic2.get((val[0],2)) != None:
                    return 0
            if val[0] == 0 and val[1] == 0:
                if dic2.get((1,1)) != None and dic2.get((2,2)) != None:
                    return 0
            if val[0] == 0 and val[1] == 2:
                if dic2.get((1,1)) != None and dic2.get((2,0)) != None:
                    return 0
    print(arr1,arr2)
    return answer