def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    while B:
        if A[0] >= B[0]:
            A.pop()
            B.pop(0)
        else:
            A.pop(0)
            B.pop(0)
            answer += 1
            
    return answer