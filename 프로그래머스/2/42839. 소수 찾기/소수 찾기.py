from itertools import permutations
def solution(numbers):
    answer = 0
    net = [True] * 10000000
    net[0] = False
    net[1] = False
    for i in range(2, 10000000):
        if not net[i]: continue 
        ni = i * 2 
        while (ni < 10000000):
            net[ni] = False
            ni = ni + i
    result = set()
    for i in range(len(numbers)):
        cases = set(permutations(list(numbers), i+1))
        for case in cases:
            case = int("".join(case))
            if net[case]:
                result.add(case)
    
    return len(result)