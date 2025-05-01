def solution(targets):
    ans = 0
    # 끝점을 기준으로 정렬
    targets.sort(key=lambda x: x[1])
    last_e = 0
    for s,e in targets:
        if s >= last_e:
            ans += 1
            last_e = e
    return ans