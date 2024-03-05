from collections import deque
def solution(m, n, puddles):
    case_data = [[0]*m for _ in range(n)]
    for wm, wn in puddles:
        case_data[wn-1][wm-1] = -1
    case_data[0][0] = 1
   		
    for i in range(n):
        for j in range(m):
            if case_data[i][j] == -1:
                continue
            if 0 <= i-1 < n and case_data[i-1][j] != -1:
                case_data[i][j] += case_data[i-1][j]
            if 0 <= j-1 < m and case_data[i][j-1] != -1:
                case_data[i][j] += case_data[i][j-1]
    answer = case_data[-1][-1] % 1000000007
    return answer