def solution(info, edges):
    ans = 0
    graph = [[] for _ in range(len(info))]
    for parent,child in edges:
        graph[parent].append(child)
    
    def dfs(idx, wolf, sheep, visitable):
        nonlocal ans,graph
        visitable.remove(idx)
        
        if info[idx] == 0:
            sheep += 1
        else:
            wolf += 1
        ans = max(ans,sheep)
        
        for child in graph[idx]:
            visitable.append(child)
        
        for child in visitable:
            if info[child] == 0:
                dfs(child,wolf,sheep,visitable[:])
            else:
                if sheep > wolf + 1:
                    dfs(child,wolf,sheep,visitable[:])
        
    dfs(0,0,0,[0])
    return ans