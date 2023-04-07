import sys
input = sys.stdin.readline

m,n = map(int,input().split())

a = [[-1 for i in range(m+2)]for i in range(n+2)]
b = [[0 for i in range(m+2)]for i in range(n+2)]
history = [[] for i in range(1000005)]


for i in range(n):
    list1 = list(map(int,input().split()))
    for j in range(len(list1)):
        a[i+1][j+1] = list1[j]
        if list1[j] == 1:
            history[0].append([i+1,j+1])
            a[i+1][j+1] += 1
            b[i+1][j+1] = 1

exitpoint = 0

for i in range(n):
    for j in range(m):
        if a[i+1][j+1] == -1:
            exitpoint += 1

if exitpoint == n*m:
    print(-1)
    sys.exit()

def bfs(q,w):
    global history
    if a[q+1][w] == 0 and b[q+1][w] == 0:
        a[q+1][w] += 1
        b[q+1][w] = b[q][w] + 1
        history[count].append([q+1,w])

    if a[q][w+1] == 0 and b[q][w+1] == 0:
        a[q][w+1] += 1
        b[q][w+1] = b[q][w] + 1
        history[count].append([q,w+1])

    if a[q-1][w] == 0 and b[q-1][w] == 0:
        a[q-1][w] += 1
        b[q-1][w] = b[q][w] + 1
        history[count].append([q-1,w])

    if a[q][w-1] == 0 and b[q][w-1] == 0:
        a[q][w-1] += 1
        b[q][w-1] = b[q][w] + 1
        history[count].append([q,w-1])

count = 0

while(history[count]):
    count += 1
    for i in history[count-1]:
        bfs(i[0],i[1])


for i in range(n):
    for j in range(m):
        if a[i+1][j+1] == 0:
            print(-1)
            sys.exit()
            
print(count-1)