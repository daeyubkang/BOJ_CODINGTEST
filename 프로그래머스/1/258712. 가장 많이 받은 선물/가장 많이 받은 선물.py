def solution(friends, gifts):
    answer = 0
    names = {}
    for i,val in enumerate(friends):
        names[val] = { "num": 0, "gifts": {}}

    

    for i in gifts:
        p1 = i.split(" ")[0]
        p2 = i.split(" ")[1]
        
        names[p1]["num"] += 1
        names[p2]["num"] -= 1

        if (names[p1]["gifts"].get(p2)):
            names[p1]["gifts"][p2] += 1
        else:
            names[p1]["gifts"][p2] = 1

        if (names[p2]["gifts"].get(p1)):
            names[p2]["gifts"][p1] -= 1
        else:
            names[p2]["gifts"][p1] = -1
    result = []
    for i, name in enumerate(friends):
        giftnum = 0
        for name2 in friends:
            if name == name2:
                continue
            else:
                if(names[name]["gifts"].get(name2)):
                    if (names[name]["gifts"].get(name2) > 0):
                        giftnum += 1
                        continue
                    elif (names[name]["gifts"].get(name2) < 0):
                        continue
                if(names[name]["num"] > names[name2]["num"]):
                    giftnum += 1
        result.append(giftnum)

    

    print(result)
    
        
    answer = max(result)
    
    return answer