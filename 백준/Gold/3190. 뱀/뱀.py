from sys import stdin, stdout
from collections import deque

read = stdin.readline
write = stdout.write

N = int(read().rstrip())
K = int(read().rstrip())

board = [[0] * (N) for _ in range(N)]

for _ in range(K):
    x, y = list(map(int, read().rstrip().split(' ')))
    board[x-1][y-1] = 1

command = deque()
L = int(read().rstrip())
for _ in range(L):
    t, c = read().rstrip().split(' ')
    t = int(t)
    command.append((t, c))

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_idx = 0
snake = deque([(0, 0)])
board[0][0] = 2
sec = 0
while True:
    x, y = snake.pop()
    snake.append((x, y))
    # 이동 후
    dir_x, dir_y = dir[dir_idx]
    x_ = dir_x + x
    y_ = dir_y + y
    # 이동 후 시간 초 증가
    sec += 1

    # 만약 부딪힌다면
    if not(0 <= x_ < N and 0 <= y_ < N) or board[x_][y_] == 2:
        write(str(sec))
        break

    snake.append((x_, y_))
    # 사과가 없다면 꼬리 부분 제거
    if board[x_][y_] == 0:
        tail_x, tail_y = snake.popleft()
        board[tail_x][tail_y] = 0
    board[x_][y_] = 2

    if command:
        time, com = command.popleft()
        if time == sec:
            if com == 'D':
                dir_idx = (dir_idx + 1) % 4
            else:
                dir_idx = (dir_idx + 3) % 4
        else:
            command.appendleft((time, com))
