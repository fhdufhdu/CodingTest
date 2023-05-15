from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n = int(read().rstrip())
power = [list(map(int, read().rsplit(' '))) for _ in range(n)]
power_sum = 0
for p in power:
    power_sum += sum(p)

min_v = 500000

def dfs(history:list):
    global min_v
    if len(history) == n//2:
        other = []
        for i in range(n):
            if i in history: continue
            other.append(i)
        a_sum = 0
        for i in range(len(history)):
            for j in range(i, len(history)):
                a = history[i]
                b = history[j]
                a_sum += power[a][b]
                a_sum += power[b][a] 

        for i in range(len(other)):
            for j in range(i, len(other)):
                a = other[i]
                b = other[j]
                a_sum -= power[a][b]
                a_sum -= power[b][a]

        min_v = min(min_v, abs(a_sum))
        return

    for i in range(history[-1] + 1, n):
        dfs(history + [i])

dfs([0])

write(str(min_v))
