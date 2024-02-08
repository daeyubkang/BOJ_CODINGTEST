def solution(cap, n, deliveries, pickups):
    answer = 0
    dic1 = []
    dic2 = []
    for i in range(n):
        if deliveries[i] != 0:
            dic1.append([i, deliveries[i]])
        if pickups[i] != 0:
            dic2.append([i, pickups[i]])

    while dic2 or dic1:
        cap1 = cap
        cap2 = cap
        arr1 = []
        arr2 = []
        maxval = 0
        if dic1:
            arr1 = [dic1.pop()]
            maxval = arr1[0][0]
        if dic2:
            arr2 = [dic2.pop()]
            maxval = max(maxval, arr2[0][0])
        while arr1:
            d1, d2 = arr1.pop()
            if d2 > cap1:
                dic1.append([d1,d2-cap1])
            elif d2 < cap1:
                if dic1:
                    arr1.append(dic1.pop())
                    cap1 -= d2
        while arr2:
            h1, h2 = arr2.pop()
            if h2 > cap2:
                dic2.append([h1,h2-cap2])
            elif h2 < cap2:
                if dic2:
                    arr2.append(dic2.pop())
                    cap2 -= h2
                    
        answer += (maxval + 1) * 2
        
        
    return answer