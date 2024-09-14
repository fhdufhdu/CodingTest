def fibo(n):
    f = [0, 1]
    i = 2
    for i in range(i, n+1):
        f.append((f[i-1] + f[i-2]) % 1234567)
    return f[-1]
    
def solution(n):
    answer = fibo(n)
    return answer