def solution(s):
    answer = ''
    arr1 = list(s.split(" "))
    minnum = int(arr1[0])
    maxnum = int(arr1[0])
    for i in range(1,len(arr1)):
        minnum = min(int(arr1[i]),minnum)
        maxnum = max(int(arr1[i]),maxnum)
    answer += str(minnum)
    answer += " "
    answer += str(maxnum)
    return answer