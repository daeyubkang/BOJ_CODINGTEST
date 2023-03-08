import sys
input = sys.stdin.readline

list1 = input()

count = 0
result = 0

for i in range(1,len(list1)):
    result += i

for i in range(1,len(list1)-1):
    a = 0
    a1 = []
    while((a+i) < len(list1)):
        a1.append(list1[a:a+i])
        a += 1
    aSort = sorted(a1)
    for j in range(len(aSort)-1):
        if aSort[j] == aSort[j+1]:
            count += 1

print(result - count)


