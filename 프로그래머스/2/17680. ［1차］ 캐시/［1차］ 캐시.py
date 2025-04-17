def solution(size, cities):
    ans = 0
    # 현 캐시 중 가장 오래 사용 안 된 거부터 교체
    # 새로운 컬럼이 캐시가 최대 사이즈일 때 들어오면, -1에 있는 거 교체하기
    # remove 후, [] + [기존]
    # 캐시 크기가 0이면 그냥 +5로
    cache = []
    for city in cities:
        if size == 0:
            ans += 5
            continue
        city = city.lower()
        # cache에 없는 경우, +5점
        if city not in cache:
            # 꽉 찼으면, 가장 사용한 지 오래된 거 제거
            if len(cache) == size:
                cache.remove(cache[0])
                cache.append(city)
            else:
                cache.append(city)
            ans += 5
        else:
            cache.remove(city)
            cache.append(city)
            ans += 1
        
    return ans