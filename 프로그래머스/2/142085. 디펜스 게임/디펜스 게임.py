import heapq
def solution(n, k, enemy):
    answer = 0
    sumvalue = 0
    heap = []
    for i,val in enumerate(enemy):
        sumvalue += val
        heapq.heappush(heap,(-val,val))
        if sumvalue > n:
            if k == 0:
                break
            sumvalue -= heapq.heappop(heap)[1]
            k -= 1
        answer = i + 1
        
    return answer