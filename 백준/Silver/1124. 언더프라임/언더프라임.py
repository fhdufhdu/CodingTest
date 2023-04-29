from sys import stdin, stdout
import time

read = stdin.readline
write = stdout.write

a, b = list(map(int, read().rsplit(' ')))

prime_net = [True for i in range(100001)]
prime_net[0] = False
prime_net[1] = False
prime_list = []
prime_list_count = [None for i in range(100001)]

for idx, is_prime in enumerate(prime_net):
    if not is_prime: continue
    prime_list.append(idx)
    current_idx = idx * 2
    while current_idx < len(prime_net):
        prime_net[current_idx] = False
        current_idx += idx

def count_prime_factorization(num:int):
    origin = num
    cnt = 0
    while num != 1:
        for p in prime_list:
            if num % p == 0: 
                cnt += 1
                num = int(num / p)
                if prime_list_count[num]:
                    cnt += prime_list_count[num]
                    num = 1
                break
    prime_list_count[origin] = cnt
    return cnt

result = 0
for i in range(a, b+1):
    cnt = count_prime_factorization(i)
    if prime_net[cnt]:
        result += 1

write(str(result))