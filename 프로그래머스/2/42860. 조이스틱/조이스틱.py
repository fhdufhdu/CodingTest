def solution(name):
    visit = [False] * len(name)
    name = list(map(lambda x:min(ord(x)-ord('A'), 26 - (ord(x)-ord('A'))), name)) 
    answer = sum(name)
    
    a = [name[i] for i in range(len(name))]
    b = [name[i] for i in range(0, -len(name), -1)]
    while a and a[-1] == 0: a.pop()
    while b and b[-1] == 0: b.pop()
    print(a, b)
    answer += min(len(a), len(b)) - 1
    if answer == -1:
        answer = 0
    return answer
def solution(name):
    answer = 0 
    for n in list(name): 
        answer += min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) 
    move_cnt_list = []
    length = len(name) 
    for i in range(length):
       	end = i + 1 
        while end < length and name[end] == 'A': end += 1
        move_cnt_list.append(i * 2 + length - end)
        move_cnt_list.append((length - end) * 2 + i)
    answer += min(move_cnt_list)
    return answer