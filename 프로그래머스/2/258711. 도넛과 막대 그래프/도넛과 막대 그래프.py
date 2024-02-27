from collections import deque

def solution(edges):
    answers = [0, 0, 0, 0]

    """
    시작 정점 구하고(output 2이상, input 0인거)
    그 정점 기반으로 그래프 시작점 구하고, 
    각 시작점에서 dfs(bfs)해서 조건보고 카운트 올리기
    """
    io = {}
    for a, b in edges:
        if a not in io:
            io[a] = [0, 1]
        else:
            io[a][1] += 1
        if b not in io:
            io[b] = [1, 0]
        else:
            io[b][0] += 1
    
    answer_0_cnt = 0 
    for v, [i, o] in io.items():
        if i == 0 and o >= 2:
            answers[0] = v 
            answer_0_cnt = o
    
    io = {}
    for a, b in edges:
        if a not in io:
            io[a] = [0, 1]
        else:
            io[a][1] += 1
        if b not in io:
            io[b] = [1, 0]
        else:
            io[b][0] += 1
        if a == answers[0]:
            del io[a]
            io[b][0] -= 1
    
    for v, [i, o] in io.items():
        if i == 0:
            answers[2] += 1
        elif i == 2 and o == 2:
            answers[3] += 1
    
    answers[1] = answer_0_cnt - (answers[2] + answers[3])
    
    return answers