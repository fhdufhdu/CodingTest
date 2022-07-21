def solution(participant, completion):
    not_completion = {}
    for p in participant:
        if p in not_completion:
            not_completion[p] += 1 
            continue
        not_completion[p] = 1
        
    for c in completion:
        if c in not_completion:
            not_completion[c] -= 1
            
    for p in participant:
        if not_completion[p] > 0:
            return p