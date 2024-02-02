from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    #먼저 딕셔너리에 모든 조합 넣기 { 조합: 점수 } 형태
    dictionary = {}
    for i in info:
        i = i.split(' ')
        for j in range(5): #조합 0개도 가능,  조합 0개일 때 딕셔너리에 ""빈문자열 형태로 저장
            combi = list(combinations(i[:4],j))
            for com in combi:
                str_value = " ".join(list(com))
                if str_value in dictionary:
                    dictionary[str_value].append(int(i[4]))
                else:
                    dictionary[str_value] = [int(i[4])]
    
    #이진탐색을 위해 미리 딕셔너리의 value값들 정렬
    for key in dictionary:
        dictionary[key].sort()
    
    answer = []
    for q in query:
        q = q.split(' and ')
        value = q[3].split(' ')
        q[3] = value[0]
        
        str_value = []
        for i in q:
            if i != '-':
                str_value.append(i)
        str_value = " ".join(str_value)
        
        if str_value in dictionary:
            result = dictionary[str_value]
            answer.append(len(result) - bisect_left(result, int(value[1])))
        else:
            answer.append(0)
            
    
    return answer