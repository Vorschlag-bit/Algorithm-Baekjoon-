from collections import Counter
def solution(weight):
    ans = 0
    counter = Counter(weight)
    for w in counter:
        if counter[w] > 1:
            ans += counter[w]*(counter[w]-1)//2
    r = [(2,3),(2,4),(3,4)]
    for w in counter:
        for a,b in r:
            t = w*a/b
            if t in counter:
                ans += counter[t]*counter[w]
    return ans