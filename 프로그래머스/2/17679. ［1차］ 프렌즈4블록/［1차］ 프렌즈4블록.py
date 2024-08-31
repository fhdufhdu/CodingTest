def solution(m, n, board):
    board = list(map(list, board))
    answer = 0
    while True:
        remove = set()
        for i in range(m-1):
            for j in range(n-1):
                if (board[i][j] != ''
                   and board[i][j] == board[i+1][j] 
                   and board[i][j] == board[i][j+1]
                   and board[i][j] == board[i+1][j+1]):
                    remove.add((i, j))
                    remove.add((i, j+1))
                    remove.add((i+1, j))
                    remove.add((i+1, j+1))
        if not remove: break
        answer += len(remove)
        for i, j in remove:
            board[i][j] = ''
        for j in range(n):
            value = []
            for i in range(m):
                if board[i][j] != '':
                    value.append(board[i][j])
            for i in range(m-1, -1, -1):
                if value:
                    board[i][j] = value.pop()
                else:
                    board[i][j] = ''
    return answer