from sys import stdin as input
from collections import defaultdict,deque
n = int(input.readline())
graph = defaultdict(list)
for _ in range(n-1):
    p,c,l = map(int, input.readline().split())
    graph[p].append((c,l))
    graph[c].append((p,l))

# 특정 노드에서 가장 먼 거리에 있는 노드와 그 거리 반환
def bfs(node):
    visit = [False] * (n+1)
    visit[node] = True
    q = deque()
    q.append((node,0))
    max_dis = 0
    max_node = node
    while q:
        cur,dis = q.popleft()
        if dis > max_dis:
            max_dis = dis
            max_node = cur
        for child,l in graph[cur]:
            if not visit[child]:
                visit[child] = True
                q.append((child,dis+l))
    return max_dis,max_node

# 루트에서 가장 먼 노드
_,node = bfs(1)
ans,_ = bfs(node)
print(ans)