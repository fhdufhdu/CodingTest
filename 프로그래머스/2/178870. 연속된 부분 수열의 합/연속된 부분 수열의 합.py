from collections import deque

def solution(sequence, k):
    answer = []
    
    seq_len = len(sequence)
    s_idx = 0
    e_idx = -1
    
    total = 0
    result = []
    while True:
        if total < k and e_idx < seq_len:
            e_idx += 1
            if e_idx < seq_len:
                total += sequence[e_idx]
        elif total == k:
            result.append((s_idx, e_idx))
            e_idx += 1
            if e_idx < seq_len:
                total += sequence[e_idx]
        elif s_idx < seq_len:
            total -= sequence[s_idx]
            s_idx += 1
        
        if s_idx >= seq_len or e_idx >= seq_len:
            break
            
    result = sorted(result, key=lambda x:(x[1]-x[0], x[0], x[1]))
    answer = result[0]
    return answer