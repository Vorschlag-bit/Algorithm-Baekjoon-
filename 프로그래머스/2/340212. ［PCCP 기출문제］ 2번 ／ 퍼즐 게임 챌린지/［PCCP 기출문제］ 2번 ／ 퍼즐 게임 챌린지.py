def solution(diffs, times, limit):
    def solve(level):
        nonlocal diffs,times,limit
        
        consume = 0
        prev = 0
        for i in range(len(diffs)):
            if level >= diffs[i]:
                consume += times[i]
                prev = times[i]
            else:
                d = (diffs[i] - level)
                consume += d * (times[i] + prev) + times[i]
                prev = times[i]
            if consume > limit: return False
        return True
    maxL = 0
    for d in diffs:
        maxL = max(maxL, d)
    # 1 ~ maxL의 이진탐색으로 최소 레벨 찾기
    minL = 1
    while minL < maxL:
        mid = (minL + maxL) // 2
        if solve(mid):
            maxL = mid
        else:
            minL = mid + 1
    print(minL)
    return minL