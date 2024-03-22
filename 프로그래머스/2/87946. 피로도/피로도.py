from itertools import permutations
def solution(k, dungeons):
    answer = -1
    # dungeons = [1, 2, 3, 4, 5, 6, 7, 8]
    cases = list(permutations(dungeons, len(dungeons)))
   	
    for case in cases:
        curr_k = k
        count = 0
        for r, c in case:
            if curr_k < r:
                break
            curr_k -= c
            count += 1
        answer = max(answer, count)
    return answer