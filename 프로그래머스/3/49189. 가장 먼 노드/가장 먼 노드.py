from collections import defaultdict,deque
def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # dis[n] = 1번 노드에서 n번 노드까지 갈 수 있는 최단 거리
    dis = [-1] * (n+1)
    q = deque()
    q.append(1)
    dis[1] = 0
    while q:
        cur_node = q.popleft()
        for nxt in graph[cur_node]:
            if dis[nxt] == -1:
                dis[nxt] = dis[cur_node] + 1
                q.append(nxt)
    md = max(dis[1:])
    return dis.count(md)