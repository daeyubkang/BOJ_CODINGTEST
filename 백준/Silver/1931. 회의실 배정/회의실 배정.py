import sys
input = sys.stdin.readline

n = int(input())
qw = [[0]*2 for i in range(n)]

for i in range(n):  
    q,w = map(int,input().split())
    qw[i][0] = w
    qw[i][1] = q

qw.sort()    
end = -1
count = 0

for i in range(n):
    if end <= qw[i][1]:
        end = qw[i][0]
        count += 1

print(count)     