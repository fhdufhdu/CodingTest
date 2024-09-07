from collections import defaultdict
def solution(str1, str2):
    answer = 1
    str1 = str1.lower()
    str2 = str2.lower()
    set1 = defaultdict(int)
    set2 = defaultdict(int)
    for i in range(len(str1)-1):
        s = ""
        for j in range(i, i+2):
            if ord('a') <= ord(str1[j]) <= ord('z'): 
                s += str1[j]
        if len(s) != 2: continue
        set1[s] += 1
    for i in range(len(str2)-1):
        s = ""
        for j in range(i, i+2):
            if ord('a') <= ord(str2[j]) <= ord('z'): 
                s += str2[j]
        if len(s) != 2: continue
        set2[s] += 1
    keys = []
    keys.extend(set1.keys())
    keys.extend(set2.keys())
    keys = set(keys)
    acount = 0
    bcount = 0
    for k in keys:
        acount += min(set1[k], set2[k])
        bcount += max(set1[k], set2[k])
    if bcount > 0:
    	answer = acount / bcount
    return int(answer * 65536)