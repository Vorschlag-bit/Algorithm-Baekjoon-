def solution(gems):
    gem = set()
    l = 0
    minStart = 0
    minL = len(gems)
    for g in gems:
        gem.add(g)
    gemd = dict()
    for r in range(len(gems)):
        gemd[gems[r]] = gemd.get(gems[r] , 0) + 1
        while len(gemd) >= len(gem):
            if r - l < minL:
                minL = r - l
                minStart = l
            gemd[gems[l]] -= 1
            if gemd[gems[l]] == 0:
                gemd.pop(gems[l])
            l += 1
    answer = [minStart + 1, minStart + minL + 1]
    return answer