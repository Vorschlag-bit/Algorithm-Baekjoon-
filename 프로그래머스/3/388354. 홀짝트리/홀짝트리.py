from collections import defaultdict,deque
def solution(nodes, edges):
    ans = [0,0]
    graph = defaultdict(list)
    for node in nodes:
        graph[node] = []
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    # 홀짝 = (번호%2 == 자식 노드 수%2)
    # 역홀짝 = (번호%2 != 자식 노드 수%2)
    # root로서 짝수 -> 자식으로서 역짝수
    # root로서 홀수 -> 자식으로서 역홀수
    # root로서 역홀수 -> 자식으로서 홀수
    # root로서 역짝수 -> 자식으로서 짝수
    visit = set()
    for node in nodes:
        if node in visit: continue
        visit.add(node)
        q = deque()
        q.append(node)
        # 홀짝
        same_tree = 0
        # 역홀짝
        diff_tree = 0
        while q:
            cur = q.popleft()
            if cur%2 == len(graph[cur])%2: same_tree += 1
            else: diff_tree += 1
            for nxt in graph[cur]:
                if nxt not in visit:
                    visit.add(nxt)
                    q.append(nxt)
        if same_tree == 1: ans[0] += 1
        if diff_tree == 1: ans[1] += 1
    return ans