from sys import stdin, stdout

read = stdin.readline
write = stdout.write

string = list(read().rstrip())

result_ = set()
def bf(remain:list, history:str):
    if len(remain) == 0:
        result_.add(history)
    for a in remain:
        if history is not None and history[-1] == a: continue
        remain_temp = [r for r in remain]
        remain_temp.remove(a)
        bf(remain_temp, a if history is None else history + a)

bf(string, None)

write(str(len(result_)))

