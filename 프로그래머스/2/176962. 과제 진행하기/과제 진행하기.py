from collections import deque

def solution(plans):
    q1 = deque()
    answer = []
    arr1 = sorted(plans, key=lambda x:x[1])
    time2 = 0
    
    for index,value in enumerate(arr1):
        time1 = 0
        num1 = int(value[1].split(":")[0])
        num2 = int(value[1].split(":")[1])
        num3 = int(value[2])
        while q1:
            qnum1 = q1[-1][1]
            qnum2 = q1[-1][2]
            qnum3 = q1[-1][3]
            qnum4 = qnum2
            qnum5 = qnum1
            qnum2 += qnum3 
            if qnum2 >= 60:
                qnum1 += qnum2//60
                qnum2 = qnum2%60
                
            if qnum1*100+qnum2 <= num1*100+num2:
                if(len(q1) > 1):
                    q1[-2][1] = q1[-1][1]
                    q1[-2][2] = q1[-1][2]+q1[-1][3]
                    if q1[-2][2] >= 60:
                        q1[-2][1] += q1[-2][2]//60
                        q1[-2][2] = q1[-2][2]%60
                answer.append(q1.pop()[0])
            else:
                time1 += (num1-qnum5)*60 + (num2-qnum4)
                q1[-1][3] -= time1
                q1.append(q1.pop())
                break

        q1.append([value[0],num1,num2,num3])
        
    for i in range(len(q1)):
        answer.append(q1.pop()[0])
    print(q1)
    
    return answer

print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
