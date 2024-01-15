def solution(arr):
    answer = []
    check_point = len(arr)
    result = [[0],[0]]
    
    def DFS(arr1):
        if( len(arr1) == 1):
            max_value = max(arr1[0])
            min_value = min(arr1[0])
        else:
            max_value = max(value for row in arr1 for value in row)
            min_value = min(value for row in arr1 for value in row)
        
        if(max_value == min_value):
            result[max_value][0] += 1
        else:
            num1 = len(arr1)//2
            part1 = [row[:num1] for row in arr1[:num1]]
            part2 = [row[num1:] for row in arr1[:num1]]
            part3 = [row[:num1] for row in arr1[num1:]]
            part4 = [row[num1:] for row in arr1[num1:]]
            DFS(part1)
            DFS(part2)
            DFS(part3)
            DFS(part4)
        
    
    DFS(arr)
    print(result)
    answer = [result[0][0],result[1][0]]
    
    return answer