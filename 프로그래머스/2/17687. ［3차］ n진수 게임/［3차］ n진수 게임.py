mapping = {
    0:'0',
    1:'1',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
    7:'7',
    8:'8',
    9:'9',
    10:'A',
    11:'B',
    12:'C',
    13:'D',
    14:'E',
    15:'F',
}
def get_number(n, num):
    if num <= 0:
        return []
    _m = num // n
    _n = num % n
    result = get_number(n, _m)
    result.append(mapping[_n])
    return result
def solution(n, t, m, p):
    answer = []
    num = 1
    numbers = ['0']
    while len(numbers) <= m*t:
        numbers.extend(get_number(n, num))
        num += 1
    for i in range(p-1, len(numbers), m):
        if len(answer) == t: break
        answer.append(numbers[i])
    return "".join(answer)