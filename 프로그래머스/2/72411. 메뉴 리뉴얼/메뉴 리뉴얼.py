from collections import Counter
from itertools import combinations as comb
def solution(orders, course):
    ans = []
    for r in course:
        org = []
        for order in orders:
            org += [c for c in comb(sorted(order),r)]
        cnt = Counter(org).most_common()
        ans += [''.join(k) for k,v in cnt if v > 1 and cnt[0][1] == v]
    return sorted(ans)