def solution(data, ext, val_ext, sort_by):
    answer = []
    if ext == "code":
        num1 = 0
    elif ext == "date":
        num1 = 1
    elif ext == "maximum":
        num1 = 2
    else:
        num1 = 3
    if sort_by == "code":
        num2 = 0
    elif sort_by == "date":
        num2 = 1
    elif sort_by == "maximum":
        num2 = 2
    else:
        num2 = 3
    for i in range(len(data)):
        if data[i][num1] < val_ext:
            answer.append(data[i])
    answer = sorted(answer, key =lambda x:x[num2])
    
    print(answer)
    return answer