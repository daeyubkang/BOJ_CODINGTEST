import sys
input = sys.stdin.readline

n = input()
count = 0
n1 = int(n)

if len(n)-1 <= 2:
        count = int(n)
elif len(n)-1 == 3:
    count = 99
    for j in range(111,n1+1):
        w3 = j//100
        w2 = (j-(w3*100))//10
        w1 = j-((j//10)*10)
        q1 = w2 - w3
        q2 = w1 - w2
        if q1 == q2:
            count += 1            

if n1 == 1000:
    count = 144

print(count)