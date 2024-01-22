def solution(s):
    answer = 0
    count1 = 1
    count2 = 0
    ch1 = list(s)[0]
    for i in range(1,len(list(s))):
        if ch1 == "":
            ch1 = list(s)[i]
            count1 = 1
            count2 = 0
            continue
        
        if ch1 == list(s)[i]:
            count1 += 1
        else:
            count2 += 1
            
        if count1 == count2:
            answer += 1
            ch1 = ""
            
    if ch1 != "":
        answer += 1
        
    
    return answer