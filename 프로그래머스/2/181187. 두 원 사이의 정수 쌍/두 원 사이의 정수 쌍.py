import math
def solution(r1, r2):
    answer = 0
    for i in range(1,r2):
        max_y = math.floor(math.sqrt(r2**2-i**2))
        if i < r1:
            if math.sqrt(r1**2-i**2) % 1 == 0:
                min_y = math.sqrt(r1**2-i**2) - 1
            else:
                min_y = math.floor(math.sqrt(r1**2-i**2))
        else:
            min_y = -1
        answer += max_y-min_y
    answer += 1
    return answer*4