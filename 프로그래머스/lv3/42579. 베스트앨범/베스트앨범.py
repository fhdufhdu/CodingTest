def solution(genres, plays): 
    data = {}
    answer = []
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre not in data:
            data[genre] = [play, [(play, i)]]
            continue
        data[genre][0] += play
        data[genre][1].append((play, i))
    
    data_values = sorted(data.values(), key=lambda x:-x[0])
    for _, l in data_values:
        l = sorted(l, key=lambda x:(-x[0], x[1]))
        if len(l) < 2:
            answer.append(l[0][1])
        else:
            answer.append(l[0][1])
            answer.append(l[1][1])
    
    return answer