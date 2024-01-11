def solution(s):
    check_num = 0
    
    for i in list(s):
        if i == "(":
            check_num+= 1
        else:
            check_num -= 1
        if check_num < 0:
            return False

    if check_num == 0:
        return True
    else:
        return False