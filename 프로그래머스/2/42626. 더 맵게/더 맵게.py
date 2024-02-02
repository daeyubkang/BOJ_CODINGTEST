import heapq
def solution(scoville, K):
    answer = 0
    arr1 = scoville
    heapq.heapify(arr1)
    while len(arr1) > 1:
        q1 = heapq.heappop(arr1)
        if q1 >= K:
            break
        q2 = heapq.heappop(arr1)
        heapq.heappush(arr1,q1+(q2*2))
        answer += 1
    if len(arr1) == 1 and arr1[0] < K:
        return -1
    return answer