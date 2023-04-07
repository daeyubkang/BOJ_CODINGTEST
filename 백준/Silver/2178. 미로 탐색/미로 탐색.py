import sys
input = sys.stdin.readline

n, m = map(int,input().split())

a = [[0 for i in range(m+2)]for j in range(n+2)]
b = [[0 for i in range(m+2)]for j in range(n+2)]

for i in range(n):
    qwe = str(input())
    for j in range(m):
        a[i+1][j+1] = int(qwe[j])

def bfs(q,w):
    global history
    if a[q+1][w] == 1 and b[q+1][w] == 0:
        b[q+1][w] = b[q][w] + 1
        history.append([q+1,w])

    if a[q][w+1] == 1 and b[q][w+1] == 0:
        b[q][w+1] = b[q][w] + 1
        history.append([q,w+1])

    if a[q-1][w] == 1 and b[q-1][w] == 0:
        b[q-1][w] = b[q][w] + 1
        history.append([q-1,w])

    if a[q][w-1] == 1 and b[q][w-1] == 0:
        b[q][w-1] = b[q][w] + 1
        history.append([q,w-1])

b[1][1] = 1
history = []
bfs(1,1)
for i in history:
    bfs(i[0],i[1])

print(b[n][m])