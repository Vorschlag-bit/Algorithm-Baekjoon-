def solution(gems):
    ans = []
    # 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간
    s = set()
    for g in gems:
        s.add(g)
    # 목표 개수
    t = len(s)
    min_l = float('inf')
    l = 0
    d = dict()
    for r in range(len(gems)):
        gem = gems[r]
        d[gem] = d.get(gem,0) + 1
        while len(d.keys()) >= t:
            remove = gems[l]
            d[remove] = d.get(remove) - 1
            if d[remove] == 0:
                del d[remove]
            l += 1
            cur_l = r + 1 - l
            if cur_l < min_l:
                ans = [l,r+1]
                min_l = cur_l
    return ans