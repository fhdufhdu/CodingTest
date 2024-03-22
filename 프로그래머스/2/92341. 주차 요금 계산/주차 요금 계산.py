from collections import defaultdict
import math
def solution(fees, records):
    dtime, dfee, utime, ufee = fees
    answer = []
    records = list(map(lambda x:x.split(' '), records))
    for idx, record in enumerate(records):
        h, m = list(map(lambda x: int(x), record[0].split(':')))
        
        records[idx][0] = h * 60 + m
    timedict = defaultdict(list)
    for t, n, io in records:
        timedict[n].append(t)
    
    for n, tl in timedict.items():
        if len(tl) & 1: tl.append(1439)
       	
        fee = dfee
        ttime = 0
        for i in range(0, len(tl), 2):
            ttime += tl[i+1] - tl[i]
        if ttime > dtime:
            fee += math.ceil((ttime - dtime) / utime) * ufee
        
        answer.append((n, fee))
    answer = list(map(lambda x:x[1],sorted(answer)))
    return answer