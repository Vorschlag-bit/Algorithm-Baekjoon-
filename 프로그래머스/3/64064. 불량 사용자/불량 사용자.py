from itertools import combinations as comb
from itertools import permutations as perm
def solution(user, bann):
    ans = 0
    
    # 조합
    for c in comb(user,len(bann)):
        # 조합 속에서 하나의 순열이라도 일치하면 ans += 1
        for perms in perm(bann,len(bann)):
            f = True
            for u,b in zip(c,perms):
                # 길이가 안 맞으면 pass
                if len(u) != len(b):
                    f = False
                    break
                for i in range(len(u)):
                    if b[i] == '*': continue
                    if b[i] != u[i]:
                        f = False
                        break
            if f:
                # print(f"찾은 순열: {perms}")
                ans += 1
                break
    
    return ans