from sys import stdin as input
from collections import defaultdict,deque
graph = defaultdict(list)
n,m = map(int,input.readline().split())

indegree = [0] * (n+1)

for _ in range(m):
    # a,b -> a가 b앞에 서야한다는 의미
    a,b = map(int,input.readline().split())
    indegree[b] += 1
    graph[a].append(b)

q = deque()
result = []
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    result.append(cur)
    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

print(' '.join(map(str, result)))