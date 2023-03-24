import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

a = list(map(int,input().split()))

countA = Counter(a)
result = [-1 for i in range(n+1)]

stackA = []

for i in range(n):
    while(stackA and countA[a[stackA[-1]]] < countA[a[i]]):
        result[stackA.pop()] = a[i]
    stackA.append(i)

for i in range(n):
    print(result[i],end=' ')