from sys import stdin, stdout
from collections import deque

read = stdin.readline
write = stdout.write

s, t = list(map(int, read().rsplit(' ')))
if s == t:
    write('0')
    exit()

deq = deque([(s, [])])
v = {s:True}

while deq:
    num, history = deq.popleft()
    if num > 10**9:
        continue

    if num == t:
        write("".join(history))
        exit()

    for oper in '*', '+', '-', '/':
        if oper == '*':
            if (num*num) in v: continue
            v.setdefault(num*num, True)
            deq.append((num*num, history+["*"]))
        elif oper == '+':
            if (num+num) in v: continue
            v.setdefault(num+num, True)
            deq.append((num+num, history+["+"]))
        elif oper == '-':
            if (num-num) in v: continue
            v.setdefault(num-num, True)
            deq.append((num-num, history+["-"]))
        elif oper == '/':
            if num == 0: continue
            if (num/num) in v: continue
            v.setdefault(num/num, True)
            deq.append((num/num, history+["/"]))

write('-1')