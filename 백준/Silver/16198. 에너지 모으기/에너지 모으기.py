from sys import stdin, stdout
import bisect

read = stdin.readline
write = stdout.write

n = int(read())
data = list(map(int, read().split()))

def foo(data : list):
    if len(data) == 3:
        return data[0] * data[2]
    sum = 0
    for i in range(1, len(data)-1):
        data_ = data[:]
        del data_[i]
        r = (data[i-1] * data[i+1]) + foo(data_)
        sum = max([r, sum])
    
    return sum

write(f'{foo(data)}\n')