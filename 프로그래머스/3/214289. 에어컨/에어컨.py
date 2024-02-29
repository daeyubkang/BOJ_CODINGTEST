def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    temperature += 10
    t1 += 10
    t2 += 10
    record = [[float('inf') for i in range(51)] for i in range(len(onboard))]
    record[0][temperature] = 0
    for i in range(0,len(onboard)-1):
        for j,val in enumerate(record[i]):
            if val != float("inf"):
                if onboard[i+1]:
                    if t1 <= j-1 <= t2:
                        if temperature < j:
                            record[i+1][j-1] = min(record[i][j],record[i+1][j-1])
                        else:
                            if t1<j:
                                record[i+1][j-1] = min(record[i][j]+a,record[i+1][j-1])
                    if t1 <= j <= t2:
                        if temperature == j:
                            record[i+1][j] = min(record[i][j],record[i+1][j])
                        else:
                            if t1<=j<=t2:
                                record[i+1][j] = min(record[i][j]+b,record[i+1][j])
                    if t1 <= j+1 <= t2:
                        if temperature > j:
                            record[i+1][j+1] = min(record[i][j],record[i+1][j+1])
                        else:
                            if j<t2:
                                record[i+1][j+1] = min(record[i][j]+a,record[i+1][j+1])
                else:
                    if temperature < j:
                        record[i+1][j-1] = min(record[i][j],record[i+1][j-1])
                    else:
                        if t1<j:
                            record[i+1][j-1] = min(record[i][j]+a,record[i+1][j-1])
                    if temperature == j:
                        record[i+1][j] = min(record[i][j],record[i+1][j])
                    else:
                        if t1<=j<=t2:
                            record[i+1][j] = min(record[i][j]+b,record[i+1][j])
                    if temperature > j:
                        record[i+1][j+1] = min(record[i][j],record[i+1][j+1])
                    else:
                        if j<t2:
                            record[i+1][j+1] = min(record[i][j]+a,record[i+1][j+1])
                    
    return min(record[-1])