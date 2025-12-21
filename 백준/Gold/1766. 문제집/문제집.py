from sys import stdin as input
from collections import defaultdict
import heapq
# n개의 문제를 모두 풀어야 한다.
# 먼저 푸는 것이 좋은 문제가 있는 문제, 먼저 푸는 문제를 반드시 먼저 풀어야 한다.
# 가능하면 쉬운 것부터 풀어야 한다.

n,m = map(int,input.readline().split())
# a,b => a문제는 b번 문제보다 먼저 푸는 게 좋음

# heap을 사용한 위상 정렬
indegree = [0] * (n+1)
# graph[a] = [b] -> b를 풀기 위해선 a를 풀어야 한다.
graph = defaultdict(list)

for _ in range(m):
    a,b = map(int,input.readline().split())
    graph[a].append(b)
    indegree[b] += 1

ans = []
q = []
for i in range(1,n+1):
    # 진입차수가 0인 작은 문제부터 heap에 넣기
    if indegree[i] == 0:
        heapq.heappush(q,i)

while q:
    cur = heapq.heappop(q)
    # 최소 힙의 원리에 따라 최솟값부터 ans에 추가됌
    ans.append(cur)
    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(q,nxt)

print(' '.join(map(str,ans)))