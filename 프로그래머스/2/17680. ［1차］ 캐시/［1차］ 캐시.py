def solution(cacheSize, cities):
    answer = 0
    cache = {}
    cities = list(map(lambda x: x.upper(), cities))
    for idx, city in enumerate(cities):
        if city in cache:
            answer += 1
            cache[city] = idx
        else:
            answer += 5
            if cacheSize > 0 and len(cache) >= cacheSize :
                items = cache.items()
                victim = min(items, key=lambda x:x[1])[0]
                del cache[victim]
            if cacheSize > 0:
                cache[city] = idx
    return answer

