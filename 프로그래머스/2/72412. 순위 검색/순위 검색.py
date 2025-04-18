from collections import defaultdict
from itertools import combinations as comb
def solution(info, query):
    ans = []
    db = defaultdict(list)
    for user_info in info:
        user = user_info.split()
        score = user[-1]
        user = user[:4]
        for r in range(5):
            for com in comb([0,1,2,3],r):
                temp = user[:]
                for c in com:
                    temp[c] = '-'
                condition = ''.join(temp)
                db[condition].append(int(score))
        
    for q in query:
        q = q.replace("and ", '')
        condition = q.split()
        score = int(condition[-1])
        condition = condition[:4]
        c = ''.join(condition)
        person = db[c]
        ans.append(sum(1 for s in person if s >= score))
        
    return ans