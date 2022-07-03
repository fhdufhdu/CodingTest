def solution(citations):
    citations = sorted(citations, reverse=True)
    answer = 0
    for i in range(len(citations)):
        if citations[i] >= (i + 1):
            if answer < (i + 1):
                answer = (i + 1)
    return answer