from collections import defaultdict
from itertools import combinations as comb
from bisect import bisect_left
def solution(info, query):
    ans = []
    db = defaultdict(list)
    for user_i in info:
        user = user_i.split()
        score = user[4]
        user = user[:4]
        # 0-3을 0~4의 조합으로 만들기
        for r in range(5):
            for com in comb([0,1,2,3],r):
                temp = user[:]
                for c in com:
                    temp[c] = '-'
                k = ''.join(temp)
                db[k].append(int(score))
    for k in db.keys():
        db[k] = sorted(db[k])
    
    for q in query:
        q = q.split()
        tx = int(q[-1])
        k = ''
        for v in q[:-1]:
            if v != 'and': k += v
        p = db[k]
        idx = bisect_left(p,tx)
        ans.append(len(p)-idx) 
    
    return ans