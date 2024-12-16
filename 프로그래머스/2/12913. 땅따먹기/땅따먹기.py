import heapq
def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            max_ = 0
            for k in range(4):
                if j == k: continue
                max_ = max(land[i][j] + land[i-1][k], max_)
            land[i][j] = max_
    return max(land[-1])