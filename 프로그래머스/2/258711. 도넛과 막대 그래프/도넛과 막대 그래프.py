from collections import defaultdict
def solution(edges):
    # 도넛그래프 => 모든 노드가 out방향이 1개
    # 막대그래프 => out 방향이 0개
    # 8자그래프 => 중심 노드는 out 방향이 2개
    in_node = defaultdict(list)
    out_node = defaultdict(list)
    center = 0
    # 중심노드 => len(out_node) >= 2 and len(in_node) == 0
    for i,o in edges:
        in_node[o].append(i)
        out_node[i].append(o)
    
    for k,v in out_node.items():
        if len(v) >= 2 and len(in_node[k]) == 0:
            center = k
    # 중심, 도넛, 막대, 8자 순
    ans = [center,0,0,0]
    
    def judge(start_node):
        nonlocal out_node
        cur_node = start_node
        while True:
            next_node = out_node[cur_node]
            
            if len(next_node) > 1: return 3
            elif len(next_node) == 0: return 2
            
            for node in next_node:
                if start_node == node: return 1
                cur_node = node
    
    for start_node in out_node[center]:
        ans[judge(start_node)] += 1
    return ans