from collections import deque,Counter
def solution(pr, t):
    q = deque()
    for idx,p in enumerate(pr):
        q.append((idx,p))
    cnt = 1
    counter = Counter(pr)
    while q:
        idx,p = q.popleft()
        m = max(counter)
        if m > p:
            q.append((idx,p))
        else:
            if idx == t:
                return cnt
            cnt += 1
            counter[p] -= 1
            if counter[p] == 0: counter.pop(p)
    return 0