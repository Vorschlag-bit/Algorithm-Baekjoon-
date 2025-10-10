def solution(stones, k):
    r = max(stones)
    l = 1
    while r >= l:
        # 최대로 건널 수 있는 사람의 수
        mid = (r+l) // 2
        flag = True
        idx = -1
        while idx < len(stones) - 1:
            move = False
            for d in range(k,0,-1):
                # 다 넘어갔다면
                if idx + d >= len(stones):
                    idx = len(stones)
                    move = True
                    break
                if stones[idx+d] >= mid:
                    idx += d
                    move = True
                    break
            if not move:
                flag = False
                break
        
        # 다 건널 수 있다면 l을 늘리기
        if flag:
            l = mid + 1
        # 다 건널 수 없다면 r을 줄이기
        else:
            r = mid - 1
    return r