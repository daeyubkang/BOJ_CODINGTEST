def solution(storey):
    answer = 0
    a = storey
    count = 1
    beforeCount = 0
    while 10**(count-1) <= a:
        num1 = (storey % (10**count)) // (10**(count-1)) + beforeCount
        if num1 > 5:
            answer += 10-num1
            beforeCount = 1
        elif num1 == 5:
            if (storey % (10**(count+1))) // (10**(count)) >= 5:
                answer += 5
                beforeCount = 1
            else:
                answer += 5
                beforeCount = 0
        else:
            answer += num1
            if beforeCount == 1 and num1 == 0:
                beforeCount = 1
            else:
                beforeCount = 0
        count += 1
    answer += beforeCount
    return answer