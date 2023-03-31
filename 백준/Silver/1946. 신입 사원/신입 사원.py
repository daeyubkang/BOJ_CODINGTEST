import sys
input = sys.stdin.readline

t = int(input())
result = []

for i in range(t):
    n = int(input())
    a = [0] * n
    count = 0
    for j in range(n):
        a[j] = list(map(int,input().split()))
    a.sort()
    num1 = a[0][1]
    for k in range(1,n):
        if a[k][1] < num1:
            num1 = a[k][1]
        else:
            count += 1
    result.append(n-count)

for i in result:
    print(i)