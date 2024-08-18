last_index = 26
dict_ = {
    chr(ord('A')+i):i+1
    for i in range(26)
}
def get_idx(i, msg):
    global last_index, dict_
    for j in range(len(msg)-i, 0, -1):
        substring = msg[i:i+j]
        if substring in dict_:
            if i+j < len(msg):
                last_index += 1
                dict_[substring+msg[i+j]] = last_index
            return dict_[substring], i+j
def solution(msg):
    answer = []
    i = 0
    while i < len(msg):
        idx, i = get_idx(i, msg)
        answer.append(idx)
    return answer