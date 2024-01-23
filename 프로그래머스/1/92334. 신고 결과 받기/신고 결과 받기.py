def solution(id_list, report, k):
    answer = []
    dic1 = {}
    dic2 = {}
    for i in id_list:
        dic1[i] = {"num": 0,"warn":{}}
        dic2[i] = 0
    for i,val in enumerate(report):
        p1 = val.split(" ")[0]
        p2 = val.split(" ")[1]
        if dic1[p2]["warn"].get(p1): continue
        else:
            dic1[p2]["num"] += 1
            dic1[p2]["warn"][p1] = 1
    for i,val in enumerate(id_list):
        if dic1[val]["num"] >= k:
            for j in dic1[val]["warn"]:
                dic2[j] += 1
    for i in dic2.values():
        answer.append(i)
    return answer