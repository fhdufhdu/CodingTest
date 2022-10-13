def get(N, cnt): 
    result = 0
    for i in range(cnt):
       	result = result * 10 + N 
    return result
def solution(N, number): 
    create_list = [[N]]
    answer = 1 
    if N == number:
        return answer
    while answer <= 8:
        answer += 1
        current_create = [get(N, answer)]
        for i in range(answer - 1):
            a = create_list[i]
            b = create_list[answer - 2 - i]
            for a_ in a:
                for b_ in b:
                    current_create.append(a_ + b_)
                    current_create.append(a_ * b_)
                    sub = a_ - b_
                    if sub > 0:
                        current_create.append(sub)
                    div = int(a_ / b_)
                    if div > 0:
                        current_create.append(div)
        create_list.append(current_create)
        for cur in current_create:
            if cur == number:
                return answer
    return -1