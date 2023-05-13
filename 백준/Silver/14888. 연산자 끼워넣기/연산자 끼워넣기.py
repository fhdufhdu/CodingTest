from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n = int(read().rstrip())
n_list = list(map(int, read().rsplit(' ')))
o = list(map(int, read().rsplit(' ')))
o_list = []

for i in range(4):
    for j in range(o[i]):
        o_list.append(i)

per_set = set()

min = 10**10
max = -10**10
def permutation(history:list):
    global min
    global max
    if len(history) == n - 1:
        history_str = ' '.join(list(map(str, history)))
        if history_str in per_set:
            return
        # print(len(per_set))
        per_set.add(history_str)

        result = n_list[0]
        for i in range(n-1):
            if history[i] == 0:
                result += n_list[i+1]
            elif history[i] == 1:
                result -= n_list[i+1]
            elif history[i] == 2:
                result = int(result * n_list[i+1])
            else:
                result = int(result / n_list[i+1])
        if result < min:
            min = result
        if result > max:
            max = result

        return

    for i in range(n - 1):
        if v[i]: continue
        v[i] = True
        permutation(history + [o_list[i]])
        v[i] = False

for i in range(n-1):
    v = [False] * (n-1)
    v[i] = True
    permutation([o_list[i]])
    v[i] = False

write(f'{max}\n{min}') 