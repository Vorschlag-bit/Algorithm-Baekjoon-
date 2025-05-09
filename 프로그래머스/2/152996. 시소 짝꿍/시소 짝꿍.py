from collections import Counter
def solution(weight):
    ans = 0
    counter = Counter(weight)
    k = sorted(counter.keys())
    for w in k:
        if counter[w] > 1:
            ans += counter[w]*(counter[w]-1)//2
    r = [(2,3),(2,4),(3,4)]
    for w in k:
        for a,b in r:
            t = w*a/b
            if t in k:
                ans += counter[t]*counter[w]
    return ans