def solution(triangle):
    answer = 0
    
    for i, row in enumerate(triangle):
        if i == 0: continue
        for j, elem in enumerate(row):
            if j == 0:
                row[j] += triangle[i - 1][j]
            elif j == len(row) - 1:
                row[j] += triangle[i - 1][-1]
            else:
                row[j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
    answer = max(row)
    return answer