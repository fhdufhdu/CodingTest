from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n, k = map(int, read().rstrip().split(' '))
numbers = list(map(int, list(read().rstrip())))

cnt = 0
stack = []
for i in range(n):
    while stack and stack[-1] < numbers[i] and cnt < k:
        stack.pop()
        cnt += 1
    stack.append(numbers[i])

while cnt < k:
    stack.pop()
    cnt += 1

for s in stack:
    write(str(s))