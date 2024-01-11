def solution(X, Y):
    X_list = [0 for i in range(10)]
    Y_list = [0 for i in range(10)]
    
    for i in list(X):
        X_list[int(i)] += 1
    
    for i in list(Y):
        Y_list[int(i)] += 1
    
    result_list = []
    for i in range(9,-1,-1):
        appendNum = min(X_list[i],Y_list[i])
        result_list.append(str(i)*appendNum)
        
    result = "".join(result_list)
    
    if result == "":
        return "-1"
    elif(result[0] == "0"):
        return "0"
    else:
        return result