from bisect import bisect_left

def solution(info, query):
    a = {"java":"0", "cpp":"1", "python":"2"}
    b = {"backend":"0", "frontend":"1"}
    c = {"junior":"0", "senior":"1"}
    d = {"chicken":"0", "pizza":"1"}
    
    results = []
    for i in info:
        lang, posi, car, food, score = i.split(" ")
        results.append([a[lang], b[posi], c[car], d[food], int(score)])
    
    r = {}
    for result in results:
        _d = "".join(result[:4])
        if (r.get(_d)):
            r[_d].append(result[4])
        else:
            r[_d] = [result[4]];

    answer = []
    s_dp = {}
    for __i in r.keys():
        s_dp[__i] = False
        
    for q in query:
        lang, posi, car, f = q.split(" and ")
        food, score = f.split(" ")
        u1 = []; u2 = []; u3 = []; u4 = []
        if (lang == "-"):
            u1.append("0"); u1.append("1"); u1.append("2");
        else:
            u1.append(a[lang])
        
        if (posi == "-"):
            u2.append("0"); u2.append("1");
        else:
            u2.append(b[posi])
        
        if (car == "-"):
            u3.append("0"); u3.append("1");
        else:
            u3.append(c[car])
        
        if (food == "-"):
            u4.append("0"); u4.append("1");
        else:
            u4.append(d[food])
        
        count = 0
        for _u1 in u1:
            for _u2 in u2:
                for _u3 in u3:
                    for _u4 in u4:
                        s = _u1 +_u2 + _u3 + _u4
                        if r.get(s):
                            arr = r[s]
                            if not s_dp[s]:
                                arr.sort()
                                s_dp[s] = True
                            f = bisect_left(arr,int(score))
                            count += len(arr) - f
        answer.append(count)
    return answer