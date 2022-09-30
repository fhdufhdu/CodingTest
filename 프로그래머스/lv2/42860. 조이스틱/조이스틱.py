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