from collections import Counter
def solution(top):
    ans = 0
    c = Counter(top)
    s = set()
    for t in top:
        s.add(t)
        c[t] -= 1
        if c[t] == 0:
            del c[t]
        if len(s) == len(c): ans += 1
    return ans