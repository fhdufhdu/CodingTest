from sys import stdin, stdout

read = stdin.readline
write = stdout.write

s = None
cnt = 0
data = None
visited = None

def subset(depth, end):
    global s, cnt
    if depth == end:
        sum = 0
        check = False
        for i in range(end):
            if visited[i] == False:
                continue
            check=True
            sum += data[i]
        if s == sum and check:
            cnt += 1
        return
    
    visited[depth] = False
    subset(depth+1, end)
    visited[depth] = True
    subset(depth+1, end)
        


n, s = map(int, read().split())
data = read().split()
data = [int(s) for s in data]
visited = [False]*n

subset(0, n)
write(f'{cnt}\n')
