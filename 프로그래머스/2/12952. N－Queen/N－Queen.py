def path(y, n, board):
    if y == n:
        return 1
    result = 0
    for i in range(n):
        av = True
        for j in range(y):
            if (board[j] == i) or (abs(i - board[j]) == abs(y - j)):
                av = False
                break
        if av:
            board[y] = i
            result += path(y+1, n, board)
    return result
				
def solution(n):
    answer = 0
    board = [-1] * n
    answer = path(0, n, board)
    return answer