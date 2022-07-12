from sys import stdin, stdout

read = stdin.readline
write = stdout.write

t = int(read().rstrip())

for _ in range(t):
    n = int(read().rstrip())
    cloths = {}
    for _ in range(n):
        name, type = read().rstrip().split(' ')
        if type not in cloths:
            cloths[type] = 1
            continue
        cloths[type] += 1
    result = 1    
    for type in cloths.keys():
        result *= (cloths[type] + 1)
    result -= 1
    write(f'{result}\n')