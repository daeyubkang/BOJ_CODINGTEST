def solution(routes):
    answer = 1
    sortarr = sorted(routes, key=lambda x:x[0])
    arr1 = sortarr[0]
    for i in range(1,len(routes)):
        if sortarr[i][0] > arr1[1]:
            answer += 1
            arr1 = sortarr[i]
        elif arr1[1] < sortarr[i][1]:
            arr1[0] = sortarr[i][0]
        else:
            arr1= sortarr[i]
            
    return answer