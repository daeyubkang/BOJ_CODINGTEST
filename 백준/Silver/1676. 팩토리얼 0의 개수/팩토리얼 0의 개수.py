import sys,math

n = int(input())

count = 0
q = 5

for i in range(1,4):
    if n//(q**i) > 0:
        count += n//(q**i)

print(count)