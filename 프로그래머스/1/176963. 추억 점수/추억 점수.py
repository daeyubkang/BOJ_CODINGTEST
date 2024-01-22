def solution(name, yearning, photo):
    answer = []
    names = {}
    for i,val in enumerate(name):
        names[val] = yearning[i]
        
    for i in photo:
        resultnum = [0]
        for j in i:
            if(names.get(j)):
                resultnum.append(names[j])
        answer.append(sum(resultnum))
                
    return answer