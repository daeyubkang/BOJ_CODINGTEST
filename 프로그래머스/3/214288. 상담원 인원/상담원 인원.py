from itertools import permutations
from itertools import combinations_with_replacement
def solution(k, n, reqs):
    answer = float('inf')
    arr1 = [[[0 for k in range(i+2)] for i in range(1+(n-k))] for j in range(k+1)]
    for a,b,c in reqs:
        for i in range(n-k+1):
            value = min(arr1[c][i][:i+1])
            x = arr1[c][i].index(value)
            if value <= a:
                arr1[c][i][x] = a+b
            else:
                arr1[c][i][-1] += arr1[c][i][x] - a
                arr1[c][i][x] += b
    
    def distribute_and_permute(k, n):
        combinations = list(combinations_with_replacement(range(1, k+1), n))

        valid_combinations = [c for c in combinations if sum(c) == k]

        all_permutations = []
        for combination in valid_combinations:
            all_permutations.extend(permutations(combination, n))

        return list(set(all_permutations))
    
    for i in distribute_and_permute(n, k):
        sumval = 0
        for j in range(k):
            sumval += arr1[j+1][i[j]-1][-1]
        if answer > sumval:
            answer = sumval
    
    return answer