import sys
input = sys.stdin.readline

n = int(input())
a = [[]for i in range(n)]

for i in range(n):
    list1 = list(map(str,input()))

    for j in range(len(list1)-1):
        if list1[j] == '(':
            a[i].append(1)
        else:
            if not a[i]:
                a[i].append("NO")
                break
            else:
                a[i].pop()

for i in range(n):
    if len(a[i]) != 0:
        print("NO")
    else:
        print("YES")