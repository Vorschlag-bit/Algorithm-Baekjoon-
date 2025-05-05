def solution(p, m):
    ml = len(m)
    ans = float('inf')
    # m 튜닝, diamond = 0, iron = 1, stone = 2
    for i,mineral in enumerate(m):
        if mineral == "diamond":
            m[i] = 0
        elif mineral == "iron":
            m[i] = 1
        else: m[i] = 2
    # 곡괭이를 사용하는 순서가 중요함 => 순열
    # 광물 인덱스, 현재 곡괭이, 사용한 곡괭이 리스트, 피로도
    def dfs(idx,hp):
        nonlocal ans,p,m
        # 기존 최소 이상이면 return
        if ans <= hp:
            return
        # 곡괭이를 다 사용하거나 모든 광물을 다 캤다면 return
        if p[0] == 0 and p[1] == 0 and p[2] == 0 or idx >= ml:
            ans = min(ans, hp)
            return
        # 다음 곡괭이 고르기
        for i in range(3):
            if p[i] == 0: continue
            p[i] -= 1
            # 곡괭이별 피로도
            consume = 0
            for j in range(idx,idx+5):
            # 현재 곡괭이로 광물 5개 캐내기
                if j < ml:
                    if i == 0:
                        consume += 1
                    elif i == 1:
                        if m[j] == 0: consume += 5
                        else: consume += 1
                    else:
                        if m[j] == 0: consume += 25
                        elif m[j] == 1: consume += 5
                        else: consume += 1
                else: break
            dfs(idx+5,hp + consume)
            p[i] += 1
    dfs(0,0)
    return ans