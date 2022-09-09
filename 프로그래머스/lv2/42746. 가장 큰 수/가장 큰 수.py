class node:
    def __init__(self, value): 
        self.value = value
    def __lt__(self, y):
        a = int(self.value + y.value)
        b = int(y.value + self.value)
        return a > b 
def solution(numbers): 
    numbers = [node(str(number)) for number in numbers]
    numbers = sorted(numbers)
    numbers = [number.value for number in numbers]
    cnt = 0
    for number in numbers:
        if number == '0':
            cnt += 1
    if len(numbers) == cnt:
    	return '0'
    else:
        return ''.join(numbers)