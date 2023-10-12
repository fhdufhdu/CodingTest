answer = [0, 0]
def solution(users, emoticons):
    global answer
    emoticon_len = len(emoticons)
    sale_per = [None] * emoticon_len
    def dfs(cnt:int, sale_per:list):
        global answer
        cnt = cnt + 1
        if cnt >= emoticon_len:
            temp_answer = [0, 0]
            for per, price in users:
                sum_price = 0
                for idx, emo_price in enumerate(emoticons):
                    if sale_per[idx] >= per:
                        sum_price += emo_price * (1-(sale_per[idx]/100))   
                if sum_price >= price:
                    temp_answer[0] += 1
                else:
                    temp_answer[1] += sum_price
            if answer[0] < temp_answer[0]:
                answer = temp_answer
            elif(
                answer[0] == temp_answer[0]
                and answer[1] < temp_answer[1]
            ):
                answer = temp_answer
            return
        for per in (10, 20, 30, 40):
            sale_per[cnt] = per
            dfs(cnt, sale_per)
    dfs(-1, sale_per)
            
    return answer