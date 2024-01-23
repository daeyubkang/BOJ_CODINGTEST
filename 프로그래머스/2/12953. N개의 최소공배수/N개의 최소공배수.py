import math

def findnum(n):
    n1 = [0]
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            n1.append(i)
            n1.append(n//i)
    return n1

def solution(arr):
    answer = 0
    arr.sort()
    num1 = arr[0]
    for i in range(1,len(arr)):
        if arr[i] % num1 == 0:
            num1 = arr[i]
        else:
            a1 = findnum(arr[i])
            a2 = findnum(num1)
            num2 = []
            for j in a1:
                for k in a2:
                    if j==k:
                        num2.append(j)
                        break
            if max(num2) == 0:
                num1 = num1 * arr[i]
            else:
                num1 = num1 * arr[i] // max(num2)
    return num1