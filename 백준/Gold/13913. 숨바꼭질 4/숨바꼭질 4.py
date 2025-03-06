from collections import deque

n,k = map(int, input().split())

l = 100000
q = deque()
visit = [-1] * (l+1)
visit[n] = 0
path = [-1] * (1+l)
q.append(n)

while q:
    idx = q.popleft()
    if idx == k:
        break
    for i in (idx-1, idx+1, idx*2):
        if 0 > i or l < i: continue
        if visit[i] == -1:
            visit[i] = visit[idx] + 1
            path[i] = idx
            q.append(i)

start = k
ans = []
while start != -1:
    ans.append(start)
    start = path[start]
ans.reverse()
print(visit[k])
print(" ".join(map(str, ans)))