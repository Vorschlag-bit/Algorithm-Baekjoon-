def solution(n, cores):
    if n <= len(cores):
        return n
    ans = 0
    l,r = 0, max(cores)*n
    t = 0
    def count(time):
        # time 기준으로 처리할 수 있는 작업량(기본적으로 0에 cores 처리)
        t = len(cores)
        for c in cores:
            t += time // c
        return t
    while l <= r:
        m = (l+r) // 2
        work = count(m)
        if work >= n:
            t = m
            r = m - 1
        else: l = m + 1
    # t-1 시간동안 수행한 작업(마지막은 작업을 알기 위해 바로 전 사이클까지만)
    w = count(t-1)
    for idx,c in enumerate(cores):
        if t%c == 0:
            w += 1
            if w == n: return idx+1
