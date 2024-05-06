from itertools import permutations
def solution(expression):
    """
    * + -
    100-200*300-500+20
    
    -
    
    20 500 
    
    연산자 우선순위가 같거나 높은 애들을 모두 스택에서 pop
    """
    answer = 0
    
    exp = []
    oper = ['-', '+', '*']
    prev = 0
    for i in range(len(expression)):
        if expression[i] in oper:
            exp.append(expression[prev:i])
            exp.append(expression[i])
            prev = i+1
    exp.append(expression[prev:])
    oper_cases = list(map(lambda x:{x[i]:i for i in range(3)},list(permutations(oper, 3))))
    
    for oper_case in oper_cases: 
        oper_s = []
        num_s = []
        for e in exp:
            if e in oper:
                while oper_s and oper_case[oper_s[-1]] >= oper_case[e]:
                    curr_oper = oper_s.pop()
                    a = num_s.pop()
                    b = num_s.pop()
                    if curr_oper == '+':
                        num_s.append(b+a)
                    elif curr_oper == '-':
                        num_s.append(b-a)
                    else:
                        num_s.append(b*a)
                oper_s.append(e)
            else:
                num_s.append(int(e))
        while oper_s:
            curr_oper = oper_s.pop()
            a = num_s.pop()
            b = num_s.pop()
            if curr_oper == '+':
                num_s.append(b+a)
            elif curr_oper == '-':
                num_s.append(b-a)
            else:
                num_s.append(b*a)
        answer = max(answer, abs(num_s[0]))
    return answer