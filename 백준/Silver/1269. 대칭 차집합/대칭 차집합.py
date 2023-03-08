import sys
input = sys.stdin.readline

a1,b1 = map(int,input().split())

a2 = list(map(int,input().split()))
b2 = list(map(int,input().split()))

count = 0

list2 = a2+b2
list3 = list(set(list2))

count = len(list2) - len(list3)

print((a1-count)+(b1-count))