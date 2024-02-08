from itertools import permutations
def solution(expression):
    answer = []
    memory = 0
    arr1 = []
    
    for i,val in enumerate(expression):
        if val == "*" or val == "+" or val == "-":
            num1 = ('').join(map(str,expression[memory:i]))
            arr1.append(int(num1))
            arr1.append(val)
            memory = i+1
        if i == len(expression) - 1:
            num1 = ('').join(map(str,expression[memory:i+1]))
            arr1.append(int(num1))
    
    arr2 = list(permutations(["+","-","*"], 3))
    for i,val in enumerate(arr2):
        result = 0
        arr3 = arr1.copy()
        for j in range(3):
            count  =  1
            while len(arr3) > 1 and count  < len(arr3):
                if arr3[count] == val[j]:
                    q1 = arr3.pop(count-1)
                    x1 = arr3.pop(count-1)
                    q2 = arr3[count-1]
                    if x1 == "+":
                        txt = q1 + q2
                        arr3[count - 1] = txt
                        if j == 2 :
                            result = txt
                    if x1 == "-":
                        txt = q1 - q2
                        arr3[count - 1] = txt
                        if j == 2 :
                            result = txt
                    if x1 == "*":
                        txt = q1 * q2
                        arr3[count - 1] = txt
                        if j == 2 :
                            result = txt
                else:
                    count += 2
        answer.append(abs(result))
        
    return max(answer)
