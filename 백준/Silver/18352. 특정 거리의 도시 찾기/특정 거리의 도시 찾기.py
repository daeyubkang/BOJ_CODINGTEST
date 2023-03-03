import sys
input = sys.stdin.readline
from collections import deque

n,m,k,x = map(int,input().split())

a = [[]for i in range(n+1)]
b = [False] * (n+1)
c = [0] * (n+1)
count = 0

for i in range(m):
    q,w = map(int,input().split())
    a[q].append(w)

def find_shortest_path(v):
    queue = deque()
    queue.append(v)
    b[v] = True
    while queue:
        now_node = queue.popleft()
        for i in a[now_node]:
            if not b[i]:
                b[i] = True
                queue.append(i)
                c[i] += c[now_node]+1          

find_shortest_path(x)
printx = False
for i in range(1,n+1):
    if c[i] == k:
        printx = True
        print(i)

if not printx:
    print(-1)