from collections import defaultdict
def solution(weights):
    answer = 0
    
    weights_dict = defaultdict(int)
    
    for weight in weights:
        weights_dict[weight] += 1
    
    for weight in weights_dict.keys():
        if weights_dict[weight] >= 2:
            answer += (weights_dict[weight] * (weights_dict[weight]-1)) // 2
        for x, y in ((4, 3), (4, 2), (3, 2)):
            temp = (weight * x) / y
            if not temp.is_integer(): continue
            if int(temp) in weights_dict:
                answer += weights_dict[int(temp)] * weights_dict[weight]
    return answer