def solution(s):
    answer = [len(s) for i in range(len(s)//2+1)]
    for i in range(1,len(s)//2+1):
        point1 = 0
        point2 = i
        beforestr = s[0:i]
        flag = False
        count = 1
        count2 = 1
        while point2+i <= len(s):
            if beforestr == s[point2:point2+i]:
                point1 = point2
                point2 = point2 + i
                count += 1
                if count//(10**count2) > 0:
                    count2 += 1
                    answer[i] += 1
                if flag:
                    answer[i] -= i
                else:
                    answer[i] -= (i - 1)
                flag = True
            else:
                point1 += i
                point2 = point1 + i
                beforestr = s[point1:point2]
                flag = False
                count = 1
                count2 = 1
    print(answer)            
    return min(answer)