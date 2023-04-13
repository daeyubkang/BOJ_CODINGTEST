import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

a = [[]for i in range(n+1)]
b = [0] * (n+1)


for i in range(m):
    q, w = map(int,input().split())
    a[q].append(w)
    a[w].append(q)

count = 0
history = []

def bfs(c):
    global count
    for i in a[c]:
        if b[i] == 0:
            count += 1
            b[i] = 1
            history.append(i)

bfs(1)

for i in history:
    bfs(i)

print(count-1)            