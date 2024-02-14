def solution(sequence):
    answer = 0
    arr1 = []
    arr2 = []
    for i in range(len(sequence)):
        if i%2>0:
            arr1.append(sequence[i] * -1)
            arr2.append(sequence[i])
        else:
            arr1.append(sequence[i])
            arr2.append(sequence[i] * -1)
    sumarr1 = [arr1[0]]
    sumarr2 = [arr2[0]]
    for i in range(1, len(sequence)):
        if arr1[i]+sumarr1[-1] < arr1[i]:
            sumarr1.append(arr1[i])
        else:
            sumarr1.append(sumarr1[-1]+arr1[i])
        if arr2[i]+sumarr2[-1] < arr2[i]:
            sumarr2.append(arr2[i])
        else:
            sumarr2.append(sumarr2[-1]+arr2[i])
            
    answer = max(max(sumarr1),max(sumarr2))
    return answer