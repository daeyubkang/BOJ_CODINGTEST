def solution(picks, minerals):
    answer = 0
    sumpicks = sum(picks)
    arr1 = []
    arr2 = [0 for i in range(len(minerals))]
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            arr2[i] = 25
        elif minerals[i] == "iron":
            arr2[i] = 5
        else:
            arr2[i] = 1
    
    point = 0
    while(sumpicks*5 > point):
        arr1.append((sum(arr2[point:point+5]),arr2[point:point+5]))
        
        point += 5
        if point + 5 > len(minerals):
            arr1.append((sum(arr2[point:]),arr2[point:]))
            break
    print(arr2, sumpicks)
    arr1 = sorted(arr1, key = lambda x:x[0], reverse=True)
    print(arr1)
    for i,val in enumerate(arr1):
        if picks[0] > 0:
            answer += len(val[1])
            picks[0] -= 1
        elif picks[1] > 0:
            for i in val[1]:
                if i == 25:
                    answer += 5
                else:
                    answer += 1
            picks[1] -= 1
        elif picks[2] > 0:
            for i in val[1]:
                if i == 25:
                    answer += 25
                elif i == 5:
                    answer += 5
                else:
                    answer += 1
            picks[2] -= 1
        else:
            break
    return answer
