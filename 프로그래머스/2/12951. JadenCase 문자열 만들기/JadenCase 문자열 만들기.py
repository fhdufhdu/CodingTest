def solution(s):
    answer = ''
    words = list(map(lambda x: list(x.strip().lower()), s.split(' ')))
    for i, word in enumerate(words):
        if word:
            word[0] = word[0].upper()
    words = list(map(lambda x: "".join(x), words))
    answer = " ".join(words)
    return answer