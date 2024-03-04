from collections import deque
def solution(people, limit):
    people = sorted(people, reverse=True)
    answer = 0
    people = deque(people)
   	
    while people:
        s = people[0]
        e = people[-1]
        if s + e <= limit and len(people) > 1:
            people.popleft()
            people.pop()
        else:
            people.popleft()
       	answer += 1
    return answer