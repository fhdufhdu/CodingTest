from collections import defaultdict
def solution(weights):
    """
    [100(1), 100(2), 100(3), 150(1), 150(2), 180, 270, 360] 이 인풋이라고 하면
    경우의 수는
    100(1), 100(2)
    100(2), 100(3)
    100(1), 100(3)
    
    150(1), 150(2)
    
    100(1), 150(1) : 3m, 2m
    100(2), 150(1) : 3m, 2m
    100(3), 150(1) : 3m, 2m
    
    100(1), 150(2) : 3m, 2m
    100(2), 150(2) : 3m, 2m
    100(3), 150(2) : 3m, 2m
    
    180, 360 : 4m, 2m
    180, 270 : 3m, 2m
    270, 360 : 4m, 3m
    
    이렇게 구할 수 있다.
    
    그래서 같은 무게가 몇명 있는지 카운트하고
    
    같은 무게의 사람이 2명 이상인 경우 조합식을 이용해서
    
    n! / ((n-2)!*2!) = (n*(n-1)) / 2! 구해서 answer에 더한다.
    
    이후 weight*4/3, weight*4/2, weight*3/2를 한 무게가
    정수이고, 존재하는 무게라면
    (왜하나면, 180 * 4 = 360 * 2, 180 * 4 / 2 = 360 이라서!)
    answer += (현재 무게를 가진 사람 * 계산 이후 나온 무게를 가진 사람)을 한다.
    """
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