import sys
input = sys.stdin.readline

a1,b1 = map(int,input().split())

a2 = list(map(int,input().split()))
b2 = list(map(int,input().split()))

count = 0

for i in b2:
    a2.append(i)

a2.sort()

for i in range(1,len(a2)):
    if a2[i] == a2[i-1]:
        count += 1

print((a1-count)+(b1-count))