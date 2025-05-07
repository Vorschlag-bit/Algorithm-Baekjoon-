from itertools import permutations as perm
def solution(k, dun):
    ans = -1
    arr = [i for i in range(len(dun))]
    for p in perm(arr,len(dun)):
        # 방문 순서
        cnt = 0
        hp = k
        for idx in p:
            if dun[idx][0] <= hp:
                hp -= dun[idx][1]
                cnt += 1
            else: break
        ans = max(cnt,ans)
    return ans