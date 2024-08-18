str_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def find_number(file):
    start_idx = 0
    end_idx = len(file)
    for i in range(len(file)-1):
        if not file[i] in str_number and file[i+1] in str_number:
            start_idx = i+1
            break
    for i in range(start_idx, len(file)-1):
        if file[i] in str_number and not file[i+1] in str_number:
            end_idx = i+1
            break
    head = file[:start_idx]
    number = file[start_idx:end_idx]
    tail = file[end_idx:]
    return head, number, tail
def solution(files):
    temp = []
    for i, file in enumerate(files):
        head, number, tail = find_number(file)
        temp.append((i, file, head.lower(), int(number)))
    temp = sorted(temp, key=lambda x: (x[2], x[3], x[0]))
    return list(map(lambda x:x[1], temp))