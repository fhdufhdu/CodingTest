from itertools import permutations, combinations
def solution(numbers):
    net = [True for i in range(10000000)]
    net[0] = False
    net[1] = False
    for i in range(2, 10000000):
       	if net[i] == True:
            
            j = i ** 2
            while j < 10000000:
                net[j] = False
                j += i
    
    perm = []
    for i in range(len(numbers)):
        perm += list(permutations(numbers, i + 1))
    available_numbers = set(map(lambda x:int("".join(x)),perm))
    
    answer = 0
    for number in available_numbers:
        if net[number] == True:
            answer += 1
    return answer