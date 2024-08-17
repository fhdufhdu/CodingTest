class Node:
    def __init__(self, number):
        self.number = number
    def __lt__(self, other):
        return self.number + other.number > other.number + self.number
def solution(numbers):
    answer = ''
    numbers = list(map(lambda x:Node(str(x)),numbers))
    numbers = list(map(lambda x:x.number, sorted(numbers)))
    answer = "".join(numbers)
    if answer[0] == "0": return "0"
    return answer