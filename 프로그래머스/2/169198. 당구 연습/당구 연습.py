def solution(m, n, startX, startY, balls):
    answer = []
    
    reflect_balls = [(-startX, startY), ((m - startX) + m, startY), (startX, -startY), (startX, (n - startY) + n)]
    for idx, (x, y) in enumerate(balls):
        ans = int(10e9)
        for rx, ry in reflect_balls:
            distance = abs(x-rx)**2 + abs(y-ry)**2
            start_ball_distance = abs(startX-rx)**2 + abs(startY-ry)**2
            if not(startX == x == rx or startY == y ==ry) or start_ball_distance < distance: 
                ans = min(distance, ans)
        answer.append(ans)
        
    return answer