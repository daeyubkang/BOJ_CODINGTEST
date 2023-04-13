import sys
input = sys.stdin.readline

n = int(input())

a = [[0 for i in range(n+2)] for i in range(n+2)]
b = [[0 for i in range(n+2)] for i in range(n+2)]

for i in range(n):
    q = str(input())
    for j in range(n):
        a[i+1][j+1] = int(q[j])

history = [[] for i in range(626)]
count = 0

def bfs(x,y):
    if a[x+1][y] == 1 and b[x+1][y] == 0:
        b[x+1][y] = 1
        history[count].append((x+1,y))
    if a[x-1][y] == 1 and b[x-1][y] == 0:
        b[x-1][y] = 1
        history[count].append((x-1,y))
    if a[x][y+1] == 1 and b[x][y+1] == 0:
        b[x][y+1] = 1
        history[count].append((x,y+1))
    if a[x][y-1] == 1 and b[x][y-1] == 0:
        b[x][y-1] = 1
        history[count].append((x,y-1))

for i in range(n):
    for j in range(n):
        if a[i+1][j+1] == 1 and b[i+1][j+1] == 0:
            b[i+1][j+1] = 1
            history[count].append((i+1,j+1))
            for k in history[count]:
                bfs(k[0],k[1])
            count += 1

print(count)
result = []
for i in range(count):
    result.append((len(history[i])))

result.sort()
for i in result:
    print(i)