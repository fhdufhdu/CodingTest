def solution(phone_book):
    length_set = set(map(lambda x: len(x), phone_book))
    d = {}
    for p in phone_book:
        d[p+"o"] = True
        for l in length_set:
            if l >= len(p): continue
            d[p[:l]+"p"] = True
    for p in phone_book:
        if p+"p" in d: return False
    return True