def solution(edges):
    # 번호 노드가 향하는 노드들 dict = {1 : [1], 2: [3,1]}
    out_node = dict()
    in_node = dict()
    # 모든 노드를 미리 등록
    for e in edges:
        out_node.setdefault(e[0], [])
        out_node.setdefault(e[1], [])
        in_node.setdefault(e[0], 0)
        in_node.setdefault(e[1], 0)
    
    for e in edges:
        start = e[0]
        end = e[1]
        out_node[start].append(end)
        in_node[end] = in_node[end] + 1
    # 중점 노드는 end가 자신인 건 없다.
    center = 0
    for start in out_node.keys():
        if in_node.get(start,0) == 0 and len(out_node[start]) >= 2:
            center = start
    # 막대 그래프 - 다음 노드 없으면 당첨
    # 도넛 - 방문 노드에 있으면 당첨
    # 8자 - out 노드 수가 2개 이상이면 당첨
    def judge(start):
        visit = set()
        cur = start
        while True:
            visit.add(cur)
            nextNodes = out_node[cur]
            
            # 8자
            if len(nextNodes) > 1:
                return 3
            # 막대
            if not nextNodes:
                return 2
            
            cur = nextNodes[0]
            # 도넛
            if cur in visit:
                return 1
        
    ans = [center,0,0,0]
    for start in out_node[center]:
        graph = judge(start)
        ans[graph] += 1
    print(ans)
    return ans