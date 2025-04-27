def solution(d, rocks, n):
    ans = 0
    rocks.sort()
    rocks += [d]
    l = 1
    r = d
    while l <= r:
        m = (l+r)//2
        cnt = 0
        position = 0
        for i in range(len(rocks)):
            rock = rocks[i]
            diff = rock - position
            if diff < m:
                cnt += 1
            else:
                position = rock
            if cnt > n:
                break
        if cnt > n:
            r = m - 1
        else:
            ans = max(ans,m)
            l = m + 1
    return ans