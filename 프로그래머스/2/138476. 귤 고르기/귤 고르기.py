from collections import Counter
def solution(k, t):
    ans = 0
    cnt = Counter(t)
    arr = []
    for c in cnt:
        # 크기, 개수
        arr.append((c,cnt[c]))
    arr.sort(key=lambda x: -x[1])
    total = 0
    for size,count in arr:
        if total >= k: break
        total += count
        ans += 1
    return ans