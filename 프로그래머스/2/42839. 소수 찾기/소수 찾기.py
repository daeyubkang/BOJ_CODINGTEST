import math
from itertools import permutations
def solution(numbers):
    answer = 0
    dic1 = {}
    def findnum(x):
        for i in range(2,int(math.sqrt(x))+1):
            if x%i == 0:
                return 0
        return 1
    arr1 = [int(i) for i in numbers]
    for i in range(1,len(numbers)+1):
        for j in permutations(arr1, i):
            if j[i-1] ==0:
                continue
            num1 = 0
            for k in range(i):
                num1 += j[k]*(10**k)
            if dic1.get(num1) != None:
                continue
            dic1[num1] = 1
            if num1 == 1:
                continue
            result = findnum(num1)
            if result == 1:
                answer += 1
    print(dic1)

    return answer