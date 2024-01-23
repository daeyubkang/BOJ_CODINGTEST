def solution(babbling):
    answer = 0
    dic1 = {"aya": 1,"ye": 1, "woo": 1, "ma": 1}
    for i,val in enumerate(babbling):
        beforebabb = ""
        count = 0
        while(val):
            if val[0] == "a":
                if val[:3] == "aya" and beforebabb != "aya":
                    beforebabb = "aya"
                    val = val[3:]
                else:
                    count += 1
            elif val[0] == "y":
                if val[:2] == "ye" and beforebabb != "ye":
                    beforebabb = "ye"
                    val = val[2:]
                else:
                    count += 1
            elif val[0] == "w":
                if val[:3] == "woo" and beforebabb != "woo":
                    beforebabb = "woo"
                    val = val[3:]
                else:
                    count += 1
            elif val[0] == "m":
                if val[:2] == "ma" and beforebabb != "ma":
                    beforebabb = "ma"
                    val = val[2:]
                else:
                    count += 1
            else: break
            
            if count == 4: break
        if val == "": answer += 1
    return answer