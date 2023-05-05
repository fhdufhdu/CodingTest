from sys import stdin, stdout

read = stdin.readline
write = stdout.write

xs, ys = list(map(int, read().rsplit(' ')))
xe, ye, dx, dy = list(map(int, read().rsplit(' ')))

min = 100000000

x = xe
y = ye

if dx == 0:
    while True:
        dis = ((xs-xe)**2 + (ys-y)**2)**0.5
        if dis <= min:
            min = dis
        else:
            y -= 1
            break
        y += 1
else:
    a = dy/dx
    b = ye - a*xe
    while True:
        y = int(a*x + b)
        dis = ((xs-x)**2 + (ys-y)**2)**0.5
        if dis <= min:
            min = dis
        else:
            x -= 1
            y = int(a*x + b)
            break
        x += 1

write(f'{x} {y}')
