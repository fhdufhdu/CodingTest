def solution(record):
    answer = []
    record = list(map(lambda x: x.split(" "), record))
    uid_to_nickname = {}
    for r in record:
        if r[0] == "Enter":
            uid_to_nickname[r[1]] = r[2]
            answer.append((r[1], "님이 들어왔습니다."))
        elif r[0] == "Leave":
            answer.append((r[1], "님이 나갔습니다."))
        else:
            uid_to_nickname[r[1]] = r[2]
    answer = list(map(lambda x: f"{uid_to_nickname[x[0]]}{x[1]}", answer))
    return answer