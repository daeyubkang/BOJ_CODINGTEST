import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

if k < n+m-1:
    print("NO")
else:
    a = [[0 for i in range(m)]for j in range(n)]
    count = 1
    for i in range(n):
        for j in range(m):
            a[i][j] = count + j
        count += 1
    
    print("YES")
    for i in range(n):
        for j in range(m):
            print(a[i][j],end=' ')
        print('')