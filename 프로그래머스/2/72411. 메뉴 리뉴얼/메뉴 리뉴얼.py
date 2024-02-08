from itertools import combinations
def solution(orders, course):
    answer = []
    for i in course:
        dic1 = {}
        maxarr = []
        maxnum = 0
        for j in orders:
            if len(j) < i:
                continue
            arrj = sorted(j)
            for k in combinations(arrj, i):
                menu = ('').join(k)
                if dic1.get(menu) == None:
                    dic1[menu] = 1
                else:
                    dic1[menu] += 1
                    if maxnum == dic1[menu]:
                        maxarr.append(menu)
                    elif maxnum < dic1[menu]:
                        maxarr = []
                        maxarr.append(menu)
                        maxnum = dic1[menu]
        for q in maxarr:
            answer.append(q)

    answer.sort()         
    return answer