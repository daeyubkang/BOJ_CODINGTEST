def solution(s, skip, index):
    answer = ''

    abc = [0 for i in range(26)]

    for i,val in enumerate(skip):
        abc[ord(val)-97] = 1
     
    for i, val in enumerate(s):
        index1 = index
        count = 0
        num1 = ord(val) - 97
        j = 0
        while j <= index1:
            if num1 + j > 25:
                if abc[(num1 + j) % 26] == 1:
                    index1 += 1
                    count += 1
            else:
                if abc[num1 + j] == 1:
                    index1 += 1
                    count += 1
            j += 1
        # for j in range(index+1,index+count+1):
        #     if num1+j > 25:
        #         if abc[(num1 + j)%26] == 1:
        #             index1 += 1
        #             count += 1

        #     else:
        #         if abc[num1 + j] == 1:
        #             index1 += 1
        #             count += 1

        num1 = ord(val) + index + count
        while num1 > 122:
            num1 -= 26
        answer += chr(num1)
    print(abc)

    return answer
