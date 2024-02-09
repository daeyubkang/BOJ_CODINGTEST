import heapq
def solution(operations):
    answer = []
    maxheap1 = []
    maxheap2 = []
    minheap1 = []
    minheap2 = []
    count = 0
    for i in operations:
        signal = i.split(" ")[0]
        num1 = int(i.split(" ")[1])
        if signal == "I":
            heapq.heappush(maxheap1,(-1*num1,num1))
            heapq.heappush(minheap1, num1)
            count += 1
        else:
            if count == 0: continue
            count -= 1
            if num1 == -1:
                while minheap2 and minheap2[0] == minheap1[0]:
                    heapq.heappop(minheap1)
                    heapq.heappop(minheap2)
                num2 = heapq.heappop(minheap1)
                heapq.heappush(maxheap2,(-1*num2,num2))
            else:
                while maxheap2 and maxheap2[0][1] == maxheap1[0][1]:
                    heapq.heappop(maxheap1)
                    heapq.heappop(maxheap2)
                num2 = heapq.heappop(maxheap1)[1]
                heapq.heappush(minheap2,num2)
    while minheap2 and minheap2[0] == minheap1[0]:
        heapq.heappop(minheap1)
        heapq.heappop(minheap2)
    while maxheap2 and maxheap2[0][1] == maxheap1[0][1]:
        heapq.heappop(maxheap1)
        heapq.heappop(maxheap2)
    if maxheap1:
        num2 = heapq.heappop(maxheap1)[1]
        heapq.heappush(minheap2,num2)
        answer.append(num2)
    while minheap2 and minheap2[0] == minheap1[0]:
        heapq.heappop(minheap1)
        heapq.heappop(minheap2)
    if minheap1:
        num2 = heapq.heappop(minheap1)
        answer.append(num2)
    while len(answer) < 2: answer.append(0)
    return answer