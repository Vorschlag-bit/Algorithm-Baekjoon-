from sys import stdin as input
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
n,r,q = map(int,input.readline().split())

# 정점 u를 루트로 하는 서브 트리에 속한 노드의 개수
cnt = [0] * (n+1)
visit = [False] * (n+1)
graph = defaultdict(list)

for _ in range(n-1):
    a,b = map(int,input.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def countSub(node):
    global cnt,visit
    cnt[node] = 1
    for child in graph[node]:
        if not visit[child]:
            visit[child] = True
            countSub(child)
            cnt[node] += cnt[child]
result = []
visit[r] = True
countSub(r)
for _ in range(q):
    node = int(input.readline())
    result.append(cnt[node])
print('\n'.join(map(str,result)))