from collections import Counter
def solution(k, tangerine):
    answer = 0
    arr1 = Counter(tangerine)
    arr2 = sorted(arr1.items(),key = lambda x:x[1], reverse=True)
    for i in list(arr2):
        if k - i[1] <= 0:
            answer += 1
            break
        k -= i[1]
        answer += 1
    return answer