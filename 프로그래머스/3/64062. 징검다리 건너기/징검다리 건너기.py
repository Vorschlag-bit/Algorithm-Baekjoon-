def solution(stones, k):
    r = max(stones)
    l = 1
    ans = 0
    while r >= l:
        # 최대로 건널 수 있는 사람의 수
        mid = (r+l) // 2
        flag = True
        # 연속 건너기가 k이상이면 실패
        ps = 0
        for s in stones:
            if s < mid:
                ps += 1
                if ps >= k:
                    flag = False
                    break
            else: ps = 0
        
        # 다 건널 수 있다면 l을 늘리기
        if flag:
            l = mid + 1
        # 다 건널 수 없다면 r을 줄이기
        else:
            r = mid - 1
    print(l,r,ans)
    return r