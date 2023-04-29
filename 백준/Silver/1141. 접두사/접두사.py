from sys import stdin, stdout
from collections import deque
import time

read = stdin.readline
write = stdout.write

n = int(read().rstrip())
word_list = [read().rstrip() for _ in range(n)]
word_list = sorted(word_list)

cnt = 0
while cnt < len(word_list):
    word = word_list[cnt]
    for i, iword in enumerate(word_list):
        if i == cnt: continue
        if iword.find(word) == 0:
            del word_list[cnt]
            cnt -= 1
            break
    cnt += 1

write(str(len(word_list)))