from collections import deque
def solution(places):
    answer = [1, 1, 1, 1, 1]
    for idx, place in enumerate(places):
        for i in range(5):
            for j in range(5):
                if place[i][j] != 'P': continue
                visit = [[False] * 5 for _ in range(5)]
                queue = deque([(i, j, 0)])
               	visit[i][j] = True
                result = 1
                while queue:
                    ci, cj, count = queue.popleft()
                    
                    if (ci, cj) != (i, j) and place[ci][cj] == 'P':
                       	if count <= 2:
                            result = 0
                        break
                    
                    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        ni, nj = ci+di, cj+dj
                        if not(0<=ni<5 and 0<=nj<5): continue
                        if visit[ni][nj]: continue
                        if place[ni][nj] == 'X': continue
                        visit[ni][nj] = True
                        queue.append((ni, nj, count+1))
                if result == 0:
                    answer[idx] = 0
                    break
    return answer