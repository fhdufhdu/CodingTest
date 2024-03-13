from itertools import permutations
check_list = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]
def check(o_or_x_temp):
    temp = o_or_x_temp
    
    for check_ in check_list:
        result = True
        for c in check_:
            result = result and (temp[c] if c in temp else False)
        if result:
            return True
    return False

def solution(board):
    answer = 1
    ox_list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] in ('O', 'X'):
                ox_list.append((i, j))
    cases = list(permutations(ox_list, len(ox_list)))
   	
    for case in cases:
        o_temp = {}
        x_temp = {}
        currect = True
        idx = 0
        if not case:
            continue
        for idx, (x, y) in enumerate(case):
            if idx & 1 and board[x][y] == 'X':
                currect = True
                x_temp[(x, y)] = True
                if check(x_temp):
                    break
            elif not(idx & 1) and board[x][y] == 'O':
                currect = True
                o_temp[(x, y)] = True
                if check(o_temp):
                    break
            else:
                currect = False
                break
        if currect and idx == len(case) - 1:
            answer = 1
            break
        else:
            answer = 0
    return answer