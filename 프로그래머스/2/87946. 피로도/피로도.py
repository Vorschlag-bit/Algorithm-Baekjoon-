from itertools import permutations as perm
def solution(k, dungeons):
    ans = -1
    n = len(dungeons)
    arr = [i for i in range(n)]
    for p in perm(arr,n):
        hp = k
        cnt = 0
        for idx in p:
            d = dungeons[idx]
            if hp < d[0]: break
            hp -= d[1]
            cnt += 1
        ans = max(ans,cnt)
    return ans