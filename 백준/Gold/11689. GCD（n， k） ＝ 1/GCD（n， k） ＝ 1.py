import math

n = int(input())

result = n

for i in range(2,int(math.sqrt(n))+1):
    if n%i ==0:
        result = result - result//i
        while(n%i==0):
            n = n//i

if n > 1:
    result = result - result//n

print(result)