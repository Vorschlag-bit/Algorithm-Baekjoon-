from collections import defaultdict
def solution(info, edges):
    ans = 1
    # 모은 양 수보다 늑대 수가 같거나 많으면 모든 양 잡아먹힘
    # 잡아먹히지 않으면서 최대의 양을 모아 다시 루트 노드로 복귀
    # 루트 노드는 항상 양(0 = 양, 1 = 늑대)
    graph = defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
    
    def dfs(no, able, wolf, sheep):
        nonlocal ans
        ans = max(ans, sheep)
        
        # 새로운 able 생성
        new_able = able.copy()
        for nxt in graph[no]:
            new_able.add(nxt)
        
        for nxt in new_able:
            if info[nxt] == 1:
                if wolf + 1 >= sheep: 
                    continue
                dfs(nxt, new_able - {nxt}, wolf+1, sheep)
            else:
                dfs(nxt, new_able - {nxt}, wolf, sheep+1)
    dfs(0,set(),0,1)
    return ans