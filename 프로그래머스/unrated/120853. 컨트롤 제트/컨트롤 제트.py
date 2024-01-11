def solution(s):
    answer = 0
    array1 = s.split(" ")
    for index,value in enumerate(array1):
        if value == "Z":
            answer -= int(array1[index-1])
        else:
            answer += int(value)
    
    
    return answer