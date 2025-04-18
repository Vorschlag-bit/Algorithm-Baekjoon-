from itertools import combinations_with_replacement
def compare(a,b):
    return a[::-1] > b[::-1]

def solution(n, info):
    ans = [-1] * 12
    for comb in combinations_with_replacement(list(range(11)), n):
        arrow = [0] * 12
        for shot in comb:
            arrow[shot] += 1
        score = 0
        for i in range(len(info)):
            ryan = arrow[i]
            apeach = info[i]
            if ryan > apeach:
                score += (10 - i)
            elif apeach >= ryan and apeach != 0:
                score -= (10 - i)
        if score <= 0: continue
        arrow[11] = score
        if compare(arrow, ans):
            ans = arrow[:]
    return ans[:11] if ans[11] != -1 else [-1]