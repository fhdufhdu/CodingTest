answer = [0, 0]	
sale_pers = None

        
def solution(users, emoticons): 
    global sale_pers
    
    def dfs(n, max_n):
        global answer, sale_pers
        n += 1
        if n >= max_n:
            temp_ans = [0, 0]
            for per, price in users:
                sum_price = 0
                for idx, emo_price in enumerate(emoticons):
                    if sale_pers[idx] < per: continue
                    sum_price += emo_price * (1 - sale_pers[idx]/100)
                if sum_price >= price:
                    temp_ans[0] += 1
                else:
                    temp_ans[1] += sum_price

            answer = max(answer, temp_ans, key=lambda x:(x[0], x[1]))
            
            return
        for per in (10, 20, 30, 40):
            sale_pers[n] = per
            dfs(n, max_n)
    
    emo_len = len(emoticons)
    sale_pers = [None] * emo_len
    dfs(-1, emo_len)
     
    return answer