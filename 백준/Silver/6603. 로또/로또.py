from sys import stdin, stdout

read = stdin.readline
write = stdout.write

all_result = []
while True:
    input = list(map(int, read().rsplit(' ')))
    k = input[0]
    s = input[1:]
    if k == 0: break
    result = []
    def find(idx:int, history:list):
        length = len(history)
        if length == 6: 
            result.append(' '.join(list(map(str, history))))
            return

        for i in range(idx + 1, len(s)):
            if length + (len(s) - i) < 6: continue
            find(i, history + [s[i]])
    
    for i in range(len(s)):
        if len(s) - i < 6: continue
        find(i, [s[i]])

    all_result.append('\n'.join(result))

write('\n\n'.join(all_result))