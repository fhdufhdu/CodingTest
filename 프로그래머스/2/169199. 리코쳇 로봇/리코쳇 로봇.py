from collections import deque
def available_route(board, curr_i, curr_j):
    routes = []
    for i in range(curr_i+1, len(board)):
        if board[i][curr_j] == 'D':       
            routes.append((i-1, curr_j))
            break
        elif i == len(board) - 1:
            routes.append((i, curr_j)) 
    for i in range(curr_i-1, -1, -1):
        if board[i][curr_j] == 'D':       
            routes.append((i+1, curr_j))
            break
        elif i == 0:
            routes.append((i, curr_j)) 
    for j in range(curr_j+1, len(board[0])):
        if board[curr_i][j] == 'D':
            routes.append((curr_i, j-1))
            break
        elif j == len(board[0]) - 1:
            routes.append((curr_i, j))
    for j in range(curr_j-1, -1, -1):
        if board[curr_i][j] == 'D':
            routes.append((curr_i, j+1))
            break
        elif j == 0:
            routes.append((curr_i, j))
    for idx, route in enumerate(routes):
        if route == (curr_i, curr_j):
            del routes[idx]
    return routes

def dfs(board, available_routes, curr_i, curr_j, visited, count):
    if board[curr_i][curr_j] == 'G':
        return count

    result = int(10e9)
    for next_i, next_j in available_routes[curr_i][curr_j]:
        if visited[next_i][next_j]: continue

        visited[next_i][next_j] = True
        result = min(dfs(board, available_routes, next_i, next_j, visited, count+1), result)
       	visited[next_i][next_j] = False
    return result
        
def solution(board):
    answer = int(10e9)
    n = len(board)
    m = len(board[0])
    board = list(map(lambda x: list(x), board))
    available_routes = [[()] * m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
	
    start_i = 0
    start_j = 0
    for i in range(n):
        for j in range(m):
            available_routes[i][j] = available_route(board, i, j)
            if board[i][j] == 'R':
                start_i = i
                start_j = j
    
    queue = deque([(start_i, start_j, 0)])
    
    while queue:
        curr_i, curr_j, count = queue.popleft()
        
        if board[curr_i][curr_j] == 'G':
            answer = min(count, answer)
        
        for next_i, next_j in available_routes[curr_i][curr_j]:
            if visited[next_i][next_j]: continue

            visited[next_i][next_j] = True
            queue.append((next_i, next_j, count + 1))

    if answer == int(10e9):
        return -1
    return answer