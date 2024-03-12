def solution(m, n, startX, startY, balls):
    answer = []
    
    reflect_balls = [(-startX, startY), ((m - startX) + m, startY), (startX, -startY), (startX, (n - startY) + n)]
    for idx, (x, y) in enumerate(balls):
        ans = int(10e9)
        for rx, ry in reflect_balls:
            distance = abs(x-rx)**2 + abs(y-ry)**2
            start_ball_distance = abs(startX-rx)**2 + abs(startY-ry)**2
            """
            1. 시작 위치, 대칭 위치, 공의 위치가 일직선 상에 없어야함
            2. (대칭 위치와 공의 위치의 사이의 거리) > (시작 위치와 대칭 위치의 거리)
               반대라면 쿠션전에 만날 수도 있음
            """
            if not(startX == x == rx or startY == y ==ry) or start_ball_distance < distance: 
                ans = min(distance, ans)
        answer.append(ans)
        
    return answer