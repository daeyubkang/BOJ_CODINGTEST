import heapq
def solution(n, works):
    answer = 0
    arr1 = []
    for i in works:
        heapq.heappush(arr1, (-i,i))
    for i in range(n):
        num1 = heapq.heappop(arr1)[1]
        if num1 == 0:
            break
        num1 -= 1
        heapq.heappush(arr1,(-num1,num1))
    print(arr1)
    for i in arr1:
        answer += i[1]*i[1]
        
    return answer