def get_digit(num):
    count = 0
    while True:
        num = num // 10
        count += 1
        if num <= 0:
            break
    return count
def solution(s):
    answer = 10e9
    for i in range(1, len(s)+1):
        groups = []
        group = []
        for j in range(0, len(s), i):
            piece = s[j:j+i]
            if group:
                if group[-1] == piece:
                	group.append(piece)
                else:
                    groups.append(group)
                    group = [piece]
            else:
                group.append(piece)
        groups.append(group)
       	
        length = 0
        # print(groups)
        for group in groups:
            if len(group) != 1:
                length += get_digit(len(group))
            length += len(group[0])
        # print(length)
        answer = min(answer, length)
                    
            
            
    return answer