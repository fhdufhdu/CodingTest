def solution(participant, completion):
    data = {}
    for p in participant:
        if p not in data:
            data[p] = 1
        else:
            data[p] += 1
    for c in completion:
        data[c] -= 1
        if data[c] == 0:
            del data[c]
    return list(data.keys())[0]