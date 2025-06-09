from collections import Counter
def solution(lottos, win):
    lc = Counter(lottos)
    # 0을 제외하고 맞춘 번호의 개수(n)  7 - n -> rank
    wc = Counter(win)
    cnt = 0
    for l in lc.keys():
        if l in wc.keys():
            cnt += 1
    worst = 7 - cnt if cnt != 0 else 6
    # cnt = 0인데, lc[0] = 0
    best = 7 - cnt - lc.get(0,0)
    if best == 7: best = 6
    return [best,worst]