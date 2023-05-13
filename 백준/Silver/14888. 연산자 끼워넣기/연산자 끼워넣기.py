from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n = int(read().rstrip())
n_list = list(map(int, read().rsplit(' ')))
oper_cnt = list(map(int, read().rsplit(' ')))

min = 10**10
max = -10**10
def recur(depth:int, result:int):
    if depth >= n - 1:
        global min
        global max
        if result < min:
            min = result
        if result > max:
            max = result
        return

    
    for j in range(4):
        if oper_cnt[j] <= 0: continue
        oper_cnt[j] -= 1
        if j == 0:
            recur(depth+1, result + n_list[depth+1])
        elif j == 1:
            recur(depth+1, result - n_list[depth+1])
        elif j == 2:
            recur(depth+1, int(result * n_list[depth+1]))
        else:
            recur(depth+1, int(result / n_list[depth+1]))
        oper_cnt[j] += 1

recur(0, n_list[0])

write(f'{max}\n{min}')