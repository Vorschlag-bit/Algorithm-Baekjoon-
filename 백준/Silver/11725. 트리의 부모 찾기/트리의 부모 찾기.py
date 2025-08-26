from sys import stdin as input
from collections import deque,defaultdict
n = int(input.readline())
graph = defaultdict(list)
for _ in range(n-1):
    a,b = map(int,input.readline().split())
    graph[a].append(b)
    graph[b].append(a)
p = dict()
p[1] = -1
q = deque()
q.append(1)
visit = [False] * (n+1)
while q:
    parent = q.popleft()
    for child in graph[parent]:
        if not visit[child]:
            visit[child] = True
            p[child] = parent
            q.append(child)
for i in range(2,n+1):
    print(p[i])