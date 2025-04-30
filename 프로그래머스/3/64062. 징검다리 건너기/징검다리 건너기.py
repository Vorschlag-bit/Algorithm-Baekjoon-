def solution(stones, k):
    ans = 0
    # 1 - k안에 건널 수 없으면 무슨 수를 써도 못 건넌다.
    l = 1
    r = max(stones)
    while l <= r:
        m = (l+r)//2
        # 연속으로 건너 뛰는 게 최대 k 이상이면 안 된다
        cross = 0
        for s in stones:
            if s < m:
                cross += 1
                if cross >= k:
                    break
            else:
                cross = 0
        if cross >= k:
            r = m - 1
        else:
            ans = max(ans,m)
            l = m + 1
    return ans