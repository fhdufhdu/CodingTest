def solution(people, limit):
    from collections import deque
    answer = 0
    people = sorted(people)
    people = deque(people) 
    while people:
       	mp = people.pop() 
        if people and mp + people[0] <= limit:
            people.popleft()
        answer += 1
            
    return answer