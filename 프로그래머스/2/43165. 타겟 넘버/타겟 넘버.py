from collections import deque
def solution(num, t):
    q = deque()
    ans = 0
    q.append((0, 0))
    while q:
        idx, cur = q.popleft()
        if idx == len(num):
            if cur == t:
                ans += 1
        else:
            q.append((idx + 1, cur + num[idx]))
            q.append((idx + 1, cur - num[idx]))
    return ans