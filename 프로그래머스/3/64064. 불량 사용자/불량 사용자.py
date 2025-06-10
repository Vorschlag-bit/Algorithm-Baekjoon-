from itertools import permutations as perm
def solution(user_id, banned_id):
    ans = set()
    n = len(user_id)
    m = len(banned_id)
    def check(p_id,b_id):
        flag = True
        for p,b in zip(p_id,b_id):
            if len(p) != len(b):
                flag = False
                break
            for pchar,bchar in zip(p,b):
                if bchar != '*' and bchar != pchar:
                    flag = False
                    break
        return flag
    # 순열로 풀기
    for p in perm(user_id, m):
        if check(p,banned_id):
            key = frozenset(p)
            ans.add(key)
    return len(ans)