from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n, k = list(map(int, read().rsplit(' ')))
words = [list(read().rstrip()) for _ in range(n)]
fix = ['a', 'n', 't', 'i', 'c'] # 고정적으로 배워야할 단어
used_letter = [False] * 26
letter2idx = lambda x:ord(x) - ord('a')
idx2letter = lambda x:chr(ord('a') + x)
for f in fix:
    used_letter[letter2idx(f)] = True

if k < 5:
    write('0')
    exit()

max_v = 0
def dfs(depth:int, i:int):
    global max_v
    if depth == k-5:
        cnt = 0
        for word in words:
            flag = True
            for l in word:
                if not used_letter[letter2idx(l)]:
                    flag = False
                    break
            if flag: cnt += 1

        max_v = max(max_v, cnt)
        return

    for idx in range(i, 26):
        if used_letter[idx]: continue
        used_letter[idx] = True
        dfs(depth+1, idx+1)
        used_letter[idx] = False


dfs(0,0)

write(str(max_v))