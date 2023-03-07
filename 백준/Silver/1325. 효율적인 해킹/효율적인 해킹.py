import sys
input = sys.stdin.readline
from collections import deque

n,e = map(int,input().split())

a = [[]for i in range(n+1)]

for i in range(e):
    q,w = map(int,input().split())
    a[w].append(q)

def findnum(start):
    count = 1
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in a[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = 1
                count += 1
    return count

max1 = 0
count2 = []
for i in range(1,n+1):
    count1 = findnum(i)
    count2.append([i,count1])
    if count1 > max1:
        max1 = count1

for i,j in count2:
    if max1 == j:
        print(i,end=" ")



