def solution(n, times):
    # 시간에 대한 이진탐색
    # 특정 시간 t에 대해서 모든 입국을 수행할 수 있는지 체크
    times.sort()
    l,r = 0, times[-1]*n
    while l <= r:
        m = (l+r) // 2
        # m 시간 안에 모든 입국을 처리할 수 있는가?
        cnt = 0
        for t in times:
            cnt += m // t
        if cnt >= n: r = m - 1
        else: l = m + 1
    return l