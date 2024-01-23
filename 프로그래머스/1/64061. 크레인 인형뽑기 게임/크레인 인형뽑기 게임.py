def solution(board, moves):
    answer = 0
    basket = [0]
    for i,val in enumerate(moves):
        val -= 1
        for j in range(len(board)):
            if board[j][val] > 0:
                basket.append(board[j][val])
                board[j][val] = 0
                break
    
    k = 0
    print(basket)
    while k < len(basket)-1:
        if basket[k] == basket[k+1]:
            basket.pop(k)
            basket.pop(k)
            answer += 2
            k -= 1
        else:
            k+=1
    print(basket)
    
    return answer