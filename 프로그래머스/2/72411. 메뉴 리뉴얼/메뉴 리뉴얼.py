from itertools import combinations as comb
from collections import Counter
def solution(orders, course):
    answer = []
    for k in course:
        comp = []
        for order in orders:
            order = sorted(order)
            for c in comb(order,k):
                comp.append(c)
        cnt = Counter(comp).most_common()
        for k,v in cnt:
            if v == cnt[0][1] and v > 1:
                answer.append(''.join(k))
    return sorted(answer)