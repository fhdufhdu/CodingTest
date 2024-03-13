from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def s_l_bfs(queue, visited, board, n, m):

    while queue:
        cur_x, cur_y, dis = queue.popleft()
        visited[cur_x][cur_y] = True

        if board[cur_x][cur_y] == 'L':
            return dis

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and board[nx][ny] != 'X':
                    queue.append((nx, ny, dis + 1))
                    visited[nx][ny] = True

    return -1


def l_e_bfs(queue, visited, board, n, m):

    while queue:
        cur_x, cur_y, dis = queue.popleft()
        visited[cur_x][cur_y] = True

        # 레버를 당겼을 때만 탈출이니까 solution() 에서 분기문으로 처리해둔 상태
        if board[cur_x][cur_y] == 'E':
            return dis

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and board[nx][ny] != 'X':
                    queue.append((nx, ny, dis + 1))
                    visited[nx][ny] = True

    return -1


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    queue = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    board = [['' for _ in range(m)] for _ in range(n)]
    start_x = start_y = lever_x = lever_y = 0

    for i in range(n):
        for j in range(m):
            split_map_line = maps[i][j:j + 1]
            board[i][j] = split_map_line

            # start, lever 위치 저장
            if split_map_line == 'S':
                start_x = i
                start_y = j

            elif split_map_line == 'L':
                lever_x = i
                lever_y = j

    # Start 좌표 Queue 에 채워넣기
    queue.append((start_x, start_y, 0))

    # Start ~ Lever 까지의 최소 거리
    start_lever_dis = s_l_bfs(queue, visited, board, n, m)
    print(f'start_lever_dis = {start_lever_dis}')

    if start_lever_dis != -1: # 레버를 당긴 상태
        # visited 초기화
        # Lever 좌표 Queue 에 채워넣기
        queue = deque()
        queue.append((lever_x, lever_y, 0))
        visited = [[False for _ in range(m)] for _ in range(n)]

        # Lever ~ Exit 까지의 최소 거리
        lever_exit_dis = l_e_bfs(queue, visited, board, n, m)
        print(f'lever_exit_dis = {lever_exit_dis}')

        if lever_exit_dis != -1: # 탈출이 가능하다면,
            return start_lever_dis + lever_exit_dis
        return -1

    else: # 레버를 당기지 못했다면,
        return -1