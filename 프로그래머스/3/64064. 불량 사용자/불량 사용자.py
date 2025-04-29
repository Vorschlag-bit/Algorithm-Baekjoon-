from itertools import combinations as comb
from itertools import permutations as perm
def check(ban,user):
    if len(ban) != len(user):
        return False
    for idx,char in enumerate(ban):
        if char == '*': continue
        if char != user[idx]:
            return False
    return True
def solution(users, ban):
    ans = 0
    # prodo, crodo = crodo, prodo <= combination
    # frodo, crodo, abc123 == crodo, frodo, abc123 <= 조합
    for c in comb(users,len(ban)):
        flag = False
        # 조합을 기반으로 순열을 생성한 뒤 하나라도 일치하면 ans+1
        for p in perm(c):
            # 조합으로 만든 순열이 일치하는지
            right = True
            for idx,b in enumerate(ban):
                # 일치하는지 판단하는 로직
                if not check(b,p[idx]):
                    right = False
                    break
            if right:
                flag = True
                break
        if flag:
            ans += 1
    return ans