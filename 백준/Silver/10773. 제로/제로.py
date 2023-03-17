import sys
input = sys.stdin.readline

n = int(input())
a = []


for i in range(n):
    m = int(input())
    if m == 0:
        if a:
            a.pop()
    else:
        a.append(m)

print(sum(a))