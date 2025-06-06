def solution(a, b, g, s, w, t):
    l = 0
    # 금 a, 은 b를 전달할 수 있는 '최소' 시간
    # 도시 개수 최대 100000
    # 특정 시간 내에 a,b를 전달할 수 있는 판단
    # 도시별 트럭의 시간당 옮길 수 있는 금,은의 양
    r = (10**9) * (10**5) * 4
    while l < r:
        m = (l+r)//2
        t_g = 0
        t_s = 0
        t_b = 0
        for i in range(len(g)):
            # 도시별 왕복횟수
            swap = m//(2*t[i])
            if m%(2*t[i]) >= t[i]: swap += 1
            # 왕복횟수 동안 옮길 수 있는 금,은,쓰까의 최대량
            t_g += min(g[i], swap*w[i])
            t_s += min(s[i], swap*w[i])
            t_b += min(g[i]+s[i], swap*w[i])
        # 운반시킬 수 있다면 하위 구간 탐색
        if t_g >= a and t_s >= b and t_b >= a+b:
            r = m
        else:
            l = m + 1  
    return l