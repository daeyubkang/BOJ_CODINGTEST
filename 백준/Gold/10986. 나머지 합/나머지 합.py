import sys
input = sys.stdin.readline
n, m = map(int,input().split())
numbers = list(map(int, input().split()))
num1 = []
sumnum = [0] * n
sumnum[0] = numbers[0]
c = [0] * m
count = 0

for i in range(1,n):
    sumnum[i] = numbers[i] + sumnum[i-1]

for i in range(n):
    num1.append(sumnum[i]%m)
    if(sumnum[i]%m==0):
        count += 1
    c[(sumnum[i]%m)] += 1

for i in range(m):
    if(c[i] > 1):
        count += (c[i] * (c[i]-1) // 2)

print(count)
