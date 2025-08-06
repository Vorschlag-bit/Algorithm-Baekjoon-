from collections import defaultdict,deque
def solution(nodes, edges):
    ans = [0,0]
    # 홀짝 트리와 역홀짝 트리 개수
    # k = 노드 번호, v = [자식 노드 번호]
    graph = defaultdict(list)
    for node in nodes:
        graph[node] = []
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    # 양방향이기에 서로 append
    # 모든 노드가 root로 두고, set을 사용해서 중복 탐사 방지
    # 부모로서 홀수 -> 자식으로서 역홀수
    # 부모로서 짝수 -> 자식으로서 역짝수
    # 부모로서 역홀수 -> 자식으로서 홀수
    # 부모로서 역짝수 -> 자식으로서 짝수
    visit = set()
    for node in nodes:
        if node in visit: continue
        visit.add(node)
        st = 0
        dt = 0
        q = deque()
        q.append(node)
        while q:
            cur = q.popleft()
            if cur % 2 == len(graph[cur]) % 2: st += 1
            else: dt += 1
            for nxt in graph[cur]:
                if nxt not in visit:
                    visit.add(nxt)
                    q.append(nxt)
        if st == 1: ans[0] += 1
        if dt == 1: ans[1] += 1
    return ans