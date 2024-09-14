def nqueen(board, curr_row, size):
    if curr_row == size:
        return 1
    result = 0
    for col in range(size):
        check = True
        for prev_row in range(curr_row):
            if board[prev_row] == col: check = False; break;
            if abs(prev_row - curr_row) == abs(board[prev_row] - col): check = False; break;
        if check:
            board[curr_row] = col
            result += nqueen(board, curr_row + 1, size)
    return result
    
def solution(n):
    answer = nqueen([0]*n, 0, n)
    return answer