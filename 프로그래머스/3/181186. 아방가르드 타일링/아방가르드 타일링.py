def solution(n):
    answer = 0
    result = [1,3,10]
    for i in range(3,9):
        sumval = 0
        for j in range(1,i+1):
            if j==1:
                point = 1
            elif j==2:
                point = 2
            elif j==3:
                point = 5
            elif j%3==0:
                point = 4
            else:
                point = 2
            sumval += result[i-j] * point
        if (i+1)%3==0:
            sumval+=4
        else:
            sumval+=2
        result.append(sumval)
    if n < 10:
        return result[n-1]
    for i in range(10,n+1):
        num1 = (result[i-2] + result[i-3]*2 + result[i-4]*6 + result[i-5] - result[i-7])%1000000007
        result.append(num1)
    answer = result[-1]
    return answer