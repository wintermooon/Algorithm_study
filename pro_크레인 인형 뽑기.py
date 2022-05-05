def solution(board, moves):
    answer = 0
    basket = []
    newboard = [[] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)-1,-1, -1):
            if board[j][i] != 0:
                newboard[i].append(board[j][i])

    for i in moves:
        if len(newboard[i-1]) == 0:
            continue
        basket.append(newboard[i-1].pop())
        if len(basket) < 2:
            continue
        if basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            answer += 2
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))