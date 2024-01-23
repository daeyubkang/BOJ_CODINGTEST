def solution(numbers, hand):
    answer = ''
    arr1 = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    lstart = [3,0]
    rstart = [3,2]
    for i,val in enumerate(numbers):
        if val in [1,4,7]:
            lstart = arr1[val]
            answer += "L"
        elif val in [3,6,9]:
            rstart = arr1[val]
            answer += "R"
        else:
            lnum1 = abs(arr1[val][0] - lstart[0])
            lnum2 = abs(arr1[val][1] - lstart[1])
            rnum1 = abs(arr1[val][0] - rstart[0])
            rnum2 = abs(arr1[val][1] - rstart[1])
            lnum3 = lnum1 + lnum2
            rnum3 = rnum1 + rnum2
            if lnum3 < rnum3:
                lstart = arr1[val]
                answer += "L"
            elif rnum3 < lnum3:
                rstart = arr1[val]
                answer += "R"
            else:
                if hand == "right":
                    rstart = arr1[val]
                    answer += "R"
                else:
                    lstart = arr1[val]
                    answer += "L"
    return answer