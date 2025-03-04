from collections import deque

n,k = map(int, input().split())

dis = [0] * 100001
visit = [False] * 100001

q = deque()
q.append((0,n))
visit[n] = True

while q:
    s,p = q.popleft()
    if p == k:
        print(s)
        break
    for i in (p * 2, p - 1, p + 1):
        if 0 <= i <= 100000 and not visit[i]:
            visit[i] = True
            if i == p*2:
                q.appendleft((s,i))
            else:
                q.append((s+1,i))
