def solution(n, stations, w):
    answer = 0
    count = 0
    count2 = 1
    while count2 <= n:
        if stations[count]-w <= count2 <= stations[count]+w:
            count2 = stations[count]+w+1
            if count<len(stations)-1:
                count += 1
        else:
            count2 += w*2+1
            answer += 1
    return answer