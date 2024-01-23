def solution(elements):
    answer = 0
    arr1 = elements * 3
    result = []
    
    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            result.append(sum(arr1[j+len(elements):j+i+len(elements)]))
    answer = len(set(result))
    return answer