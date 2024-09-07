from collections import defaultdict
def solution(n, words):
    answer = [0, 0]
    say = defaultdict(lambda: False)
    prev_word = words[0][0]
    for idx, word in enumerate(words):
        if (
            len(word) <= 1
            or word[0] != prev_word[-1]
            or say[word]
        ):
            answer = [idx % n + 1, idx // n + 1]
            break
        prev_word = word
        say[word] = True
    return answer