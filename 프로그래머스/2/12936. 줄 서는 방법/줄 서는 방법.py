def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def run(data, k):
    n = len(data)
    p = factorial(n)
    for i in range(1, n+1):
        if (p // n) * i >= k:
            k = k - ((p // n) * (i-1))
            break
    num = data[i-1]
    del data[i-1]
    return (num, data, k)

def solution(n, k):
    answer = []
    data = [i+1 for i in range(n)]
    for i in range(n):
        result, data, k = run(data, k)
        answer.append(result) 
            
    return answer