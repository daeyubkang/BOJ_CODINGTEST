def solution(s):
    answer = []
    arr1 = []
    dic1 = {}
    s = s.replace("{","")
    s = s.split("}")
    s = sorted(s, key=len)
    s.pop(0)
    s.pop(0)
    for i in range(len(s)):
        if s[i][0] == ",":
            s[i] = s[i][1:]
        if s[i].find(",") == -1:
            k = int(s[i])
            dic1[k] = 1
            answer.append(k)
            continue
        for j in s[i].split(","):
            j = int(j)
            if dic1.get(j) == None:
                dic1[j] = 1
                answer.append(j)
            else:
                continue
    return answer