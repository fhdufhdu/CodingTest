import itertools

def solution(users, emoticons):
    """
    할인율을 중복 허용해서 이모티콘 갯수만큼 뽑음
    만약 할인율이 [1, 2]이고 이모티콘 갯수가 3개라면
    2 * 2 * 2 = 8개의 경우의 수가 나옴 이걸 모두 계산하는거임
    """
    cases = itertools.product([10, 20, 30, 40], repeat=len(emoticons))
    cases = list(cases)
   	
    answer = (0, 0)
    for case in cases:
        plus_user_cnt = 0
        total_emoticon_price = 0
        for want_percent, max_price in users: 
            user_price_total = 0 
            for sale_percent, emoticon_price in zip(case, emoticons):
                if sale_percent >= want_percent:
                    user_price_total += emoticon_price * (1-(sale_percent/100))
            if user_price_total >= max_price:
                plus_user_cnt += 1
            else:
                total_emoticon_price += user_price_total
        result = (plus_user_cnt, total_emoticon_price)
        if answer < result:
            answer = result 
            
    return list(answer)