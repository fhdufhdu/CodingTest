from collections import deque
from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n = int(read().rstrip())
data = [list(map(int, read().rsplit(' '))) for _ in range(n)]

oper_list = []
def dfs(history:list):
    if len(history) == 5:
        oper_list.append(history)
        return
    
    for i in range(4):
        dfs(history + [i])

dfs([])
max_v = 0
for oper in oper_list:
    dd = [[data[i][j] for j in range(n)]for i in range(n)]
    for o in oper:
        if o == 0:
            for i in range(n):
                deq = deque(dd[i])
                ddd = []
                while deq:
                    num = deq.popleft()
                    if num == 0:
                        continue
                    if ddd and ddd[-1][0] == num and ddd[-1][1] == 0:
                            ddd[-1][0] += num
                            ddd[-1][1] = 1
                    else:
                        ddd.append([num,0])
                for _ in range(n - len(ddd)):
                    ddd.append([0,0])
                dd[i] = list(map(lambda x:x[0], ddd))
        elif o == 1:
            for i in range(n):
                deq = dd[i]
                ddd = []
                while deq:
                    num = deq.pop()
                    if num == 0:
                        continue
                    if ddd and ddd[-1][0] == num and ddd[-1][1] == 0:
                            ddd[-1][0] += num
                            ddd[-1][1] = 1
                    else:
                        ddd.append([num, 0])
                for _ in range(n - len(ddd)):
                    ddd.append([0, 0])
                ddd.reverse()
                dd[i] = list(map(lambda x:x[0], ddd))
        elif o == 2:
            for i in range(n):
                deq = deque([dd[j][i] for j in range(n)])
                ddd = []
                while deq:
                    num = deq.popleft()
                    if num == 0:
                        continue
                    if ddd and ddd[-1][0] == num and ddd[-1][1] == 0:
                            ddd[-1][0] += num
                            ddd[-1][1] = 1
                    else:
                        ddd.append([num, 0])
                for _ in range(n - len(ddd)):
                    ddd.append([0, 0])
                for j in range(n):
                    dd[j][i] = ddd[j][0]
        elif o == 3:
            for i in range(n):
                deq = [dd[j][i] for j in range(n)]
                ddd = []
                while deq:
                    num = deq.pop()
                    if num == 0:
                        continue
                    if ddd and ddd[-1][0] == num and ddd[-1][1] == 0:
                            ddd[-1][0] += num
                            ddd[-1][1] = 1
                    else:
                        ddd.append([num, 0])
                for _ in range(n - len(ddd)):
                    ddd.append([0, 0])
                ddd.reverse()
                for j in range(n):
                    dd[j][i] = ddd[j][0]
    for i in range(n):
         for j in range(n):
                max_v = max(max_v, dd[i][j])
write(str(max_v))
