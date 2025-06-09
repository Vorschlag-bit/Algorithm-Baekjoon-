def solution(routes):
    ans = 0
    # 가장 많이 겹치는 구간들만 어떻게?
    routes.sort(key=lambda x: x[1])
    l_e = -30001
    for s,e in routes:
        if s > l_e:
            l_e = e
            ans += 1
    return ans