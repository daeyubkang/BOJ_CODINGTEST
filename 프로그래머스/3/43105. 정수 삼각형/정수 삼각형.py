def solution(triangle):
    answer = 0
    arr1 = []
    arr2 = []
    for i,val in enumerate(triangle):
        if i == 0: 
            arr1.append(val[0]) 
            continue
        if arr1:
            for j in range(len(arr1)):
                if j == 0:
                    arr2.append(arr1[0]+val[0])
                else:
                    arr2.append(max(arr1[j],arr1[j-1])+val[j])
            arr2.append(arr1[-1]+val[-1])
            arr1 = []
        else:
            for j in range(len(arr2)):
                if j == 0:
                    arr1.append(arr2[0]+val[0])
                else:
                    arr1.append(max(arr2[j],arr2[j-1])+val[j])
            arr1.append(arr2[-1]+val[-1])
            arr2 = []
    if arr1:
        answer = max(arr1)
    else:
        answer = max(arr2)
    return answer