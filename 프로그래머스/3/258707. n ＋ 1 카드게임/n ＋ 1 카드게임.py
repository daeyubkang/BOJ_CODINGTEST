from collections import deque
def solution(coin, cards):
    answer = 0
    cardcount = 0
    n = len(cards)
    dic1 = {}
    flag = False
    arr1 = deque()
    for i,val in enumerate(cards):
        if i < (n//3):
            dic1[val] = [0,0]
        else:
            dic1[val] = [((i-(n//3))//2)+1,0]
    for i,val in enumerate(cards):
        if i < (n//3):
            if dic1[(n+1)-val][1]==0 and dic1[(n+1)-val][0] == 0:
                dic1[val][1] = 1
                cardcount += 1
        else:
            answer = dic1[val][0]
            if dic1[(n+1)-val][0] < dic1[val][0]:
                if dic1[(n+1)-val][0] == 0:
                    arr1.append(1)
                else:
                    arr1.appendleft(2) 
            elif dic1[(n+1-val)][1]==0 and dic1[(n+1)-val][0] == dic1[val][0]:
                arr1.appendleft(2)
                dic1[val][1] = 1
            if i%2==0: continue
            if cardcount>0:
                cardcount -= 1
                continue
            else:
                if arr1:
                    coin1 = arr1.pop()
                    if coin1 > coin:
                        flag = True
                        break
                    else:
                        coin -= coin1
                else: 
                    flag = True
                    break 
    if not flag: answer+=1    
    return answer