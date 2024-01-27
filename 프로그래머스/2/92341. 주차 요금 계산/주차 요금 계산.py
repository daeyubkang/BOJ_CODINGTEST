def solution(fees, records):
    answer = []
    dic1 = {}
    arr1 = []
    for i,val in enumerate(records):
        time = (int(val.split(" ")[0].split(":")[0])*60) + int(val.split(" ")[0].split(":")[1])
        carnum = val.split(" ")[1]
        inout = val.split(" ")[2]
        if dic1.get(carnum) == None:
            dic1[carnum] = {"inout": inout, "time": time, "sumtime": 0}
        else:
            if dic1[carnum]["inout"] == "IN":
                dic1[carnum]["sumtime"] += time - dic1[carnum]["time"]
                dic1[carnum]["inout"] = ""
            else:
                dic1[carnum]["inout"] = inout
                dic1[carnum]["time"] = time
    maxtime = 23*60 + 59
    for i,val in enumerate(dic1):
        pay = 0
        if dic1[val]["inout"] == 'IN':
            sumtime2 = (maxtime - dic1[val]["time"]) + dic1[val]["sumtime"]
        else:
            sumtime2 = dic1[val]["sumtime"]
        pay = fees[1]
        if sumtime2-fees[0] >= 0:
            if (sumtime2-fees[0])%fees[2] > 0:
                pay += ((sumtime2-fees[0])//fees[2]+1) * fees[3]
            else:
                pay += ((sumtime2-fees[0])//fees[2]) * fees[3]
        arr1.append((val,pay))
    arr1 = sorted(arr1, key=lambda x:x[0])
    for i in arr1:
        answer.append(i[1])
    return answer