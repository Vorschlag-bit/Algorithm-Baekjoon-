def solution(n, times):
    ans = float('inf')
    # 이진탐색의 대상이 되는 건? => 모든 사람이 심사 소요 시간
    # 모든 사람의 심사 소요 최대 시간? => 1 ~ 
    times.sort()
    r = n * times[-1]
    l = 1
    while l <= r:
        m = (l+r)//2
        cnt = 0
        for i in range(len(times)-1,-1,-1):
            cnt += m // times[i]
        if cnt >= n:
            r = m - 1
            ans = min(ans,m)
        else:
            l = m + 1
    return ans