def solution(n, wires):
    answer = 10e9
    g = [[] for _ in range(n+1)]
    for a, b in wires:
        g[a].append(b)
        g[b].append(a)
    for a, b in wires:
        visit = [False] * (n + 1)
        cnts = []
        for i in range(1, n + 1):
            if visit[i]: continue
            stack = [i]
            visit[i] = True
            cnt = 1
            while stack:
                curr = stack.pop()
                for _next in g[curr]:
                    if visit[_next]: continue
                    if (curr, _next) in [(a, b), (b, a)]: continue
                    stack.append(_next)
                    visit[_next] = True
                    cnt += 1
            cnts.append(cnt)
        answer = min(answer, abs(cnts[0]-cnts[1]))
    return answer