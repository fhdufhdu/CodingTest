def get_sounds(sheet):
    sheet = list(sheet)
    result = []
    while sheet:
        last = sheet.pop()
        if (last == "#"): last = sheet.pop()+last
        result.append(last)
    return list(reversed(result))

def get_minutes(time):
    hours, minutes = map(lambda x: int(x), time.split(":"))
    return hours * 60 + minutes

def check(m1, m2):
    m1_len = len(m1)
    m2_len = len(m2)
    if m1_len > m2_len: return False
    
    for i in range(m2_len - m1_len + 1):
        check = True
        for j in range(m1_len):
            check = check and (m2[i+j] == m1[j])
        if check: return True
    return False
    
def solution(m, musicinfos):
    answer = ''
    m = get_sounds(m)
    result = []
    for idx, musicinfo in enumerate(musicinfos):
        start, end, title, sheet = musicinfo.split(",")
        sheet = get_sounds(sheet)
        time = get_minutes(end) - get_minutes(start)
        melody = []
        for i in range(time):
            melody.append(sheet[i % len(sheet)])
        if check(m, melody):
            result.append((-time, idx, title))
    result = sorted(result)
    if not result: return "(None)"
    return result[0][2]