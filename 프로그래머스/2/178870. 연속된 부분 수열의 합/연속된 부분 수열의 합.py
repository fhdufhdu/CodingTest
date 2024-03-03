def solution(sequence, k):
    start_idx = 0
    end_idx = 0
    
    total = sequence[0]
    answer = []
    seq_len = len(sequence)
    while True:
        if total < k and end_idx < seq_len - 1:
            end_idx += 1
            total += sequence[end_idx]
        else:
            if total == k:
                answer.append([start_idx, end_idx])
            total -= sequence[start_idx]
            start_idx += 1
        if start_idx > end_idx:
            break
    
    answer = sorted(answer, key=lambda x: (x[1]-x[0], x[0], x[1]))
    return answer[0]