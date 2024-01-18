def solution(sequence, k):
    answer = [0,len(sequence)]
    point1 = 0
    point2 = 0
    minresult = len(sequence)
    # sumarr = [[0] for i in range(len(sequence))]
    # for i,val in enumerate(sequence):
    #     sumarr[i] = sum
    sumresult = sequence[0]
    while(point1 < len(sequence)):
        if sumresult > k:
            sumresult -= sequence[point1]
            point1 += 1
            if point1  > point2:
                point2 += 1
                break
        elif sumresult < k:
            if point2 >= len(sequence)-1:
                break
            point2 += 1
            sumresult += sequence[point2]
        else:
            if point1 == point2:
                answer = [point1,point2]
                break
            if minresult > point2 - point1:
                minresult = point2 -point1
                answer = [point1,point2]
            if point2 == len(sequence) - 1:
                break
            sumresult -= sequence[point1]
            point1 +=1
            point2 += 1
            sumresult += sequence[point2]
    
    return answer