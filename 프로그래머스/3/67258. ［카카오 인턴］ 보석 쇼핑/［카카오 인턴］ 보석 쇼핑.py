from collections import deque
def solution(gems):
    answer = []
    arr1 = deque()
    dic1 = {}
    count = 0
    countcheck = 0
    for i in gems:
        if dic1.get(i) == None:
            dic1[i] = 0
            count += 1
    for i, gem in enumerate(gems):
        dic1[gem] += 1
        arr1.append([gem,i])
        if dic1[gem] == 1:
            countcheck += 1
        while dic1[arr1[0][0]] > 1:
            dic1[arr1[0][0]] -= 1
            arr1.popleft()
        if count == countcheck:
            if not answer:
                answer = [arr1[0][1]+1, arr1[-1][1]+1]
            else:
                if arr1[-1][1] - arr1[0][1] < answer[1] - answer[0]:
                    answer = [arr1[0][1]+1, arr1[-1][1]+1]
    return answer
