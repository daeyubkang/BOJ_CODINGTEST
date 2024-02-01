def solution(edges):
    answer = [0,0,0,0]
    arr1 = [0 for i in range(len(edges)+2)]
    arr2 = [[] for i in range(len(edges)+2)]
    arr3 = [[] for i in range(len(edges)+2)]
    start = []
    for i,val in enumerate(edges):
        arr1[val[0]] += 1
        arr1[val[1]] -= 1
        arr2[val[0]].append(val[1])
        arr3[val[1]].append(val[0])
    rootnum = arr1.index(max(arr1))
    answer[0] = rootnum
    
    for i in arr2[rootnum]:
        start.append(i)
        arr3[i].remove(rootnum)
            
    for i,val in enumerate(start):
        circle = val
        val = -1
        typegr = 1
        count = 0
        while val != circle:
            if count==0: val=circle
            line = len(arr2[circle])
            line2 = len(arr3[circle])
            if line == 0 or line2 == 0:
                typegr = 2
                break
            if line > 1:
                typegr = 3
                break
            circle = arr2[circle][0]
            count += 1
        answer[typegr] += 1
    
    return answer