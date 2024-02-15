def solution(n, k, cmd):
    answer = ''
    removearr = []
    linkedlist = [[None,1]]
    for i in range(1,n-1):
        linkedlist.append([i-1,i+1])
    linkedlist.append([n-2,None])
    removecount = 0
    firstpoint = 0
    lastpoint = n-1
    for i in cmd:
        if i=="Z":
            removecount -= 1
            removenum = removearr.pop()
            if linkedlist[removenum][0] == None:
                linkedlist[linkedlist[removenum][1]][0] = removenum
                firstpoint = removenum
            elif linkedlist[removenum][1] == None:
                linkedlist[linkedlist[removenum][0]][1] = removenum
                lastpoint = removenum
            else:
                linkedlist[linkedlist[removenum][0]][1] = removenum
                linkedlist[linkedlist[removenum][1]][0] = removenum
        elif i=="C":
            removearr.append(k)
            if k==firstpoint:
                linkedlist[linkedlist[k][1]][0] = None
                k=linkedlist[k][1]
                firstpoint = k
            elif k==lastpoint:
                linkedlist[linkedlist[k][0]][1] = None
                k=linkedlist[k][0]
                lastpoint = k
            else:
                linkedlist[linkedlist[k][0]][1] = linkedlist[k][1]
                linkedlist[linkedlist[k][1]][0] = linkedlist[k][0]
                k=linkedlist[k][1]
            removecount += 1
        elif i[0]=="U":
            count = int(i.split(" ")[1])
            if count > n-removecount:
                count = count%(n-removecount)
            for i in range(count):
                if linkedlist[k][0] == None:
                    k=lastpoint
                else:
                    k = linkedlist[k][0]
        else:
            count = int(i.split(" ")[1])
            if count > n-removecount:
                count = count%(n-removecount)
            for i in range(count):
                if linkedlist[k][1] == None:
                    k=firstpoint
                else:
                    k = linkedlist[k][1]

    resultarr = ["O" for i in range(n)]
    for i in removearr:
        resultarr[i] = "X"
    answer = ("").join(resultarr)
    return answer