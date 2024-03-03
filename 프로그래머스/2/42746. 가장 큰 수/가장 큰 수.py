class Node:
    def __init__(self, number):
        self.number = number
    def __lt__(self, node):
        a = int(f"{self.number}{node.number}")
        b = int(f"{node.number}{self.number}")
        return a > b
       	 
def solution(numbers):
    numbers = list(map(lambda x: Node(x), numbers))
    numbers = sorted(numbers)
    answer = "".join(list(map(lambda x: str(x.number), numbers)))
    
    if answer[0] == '0':
        return '0'
    return answer