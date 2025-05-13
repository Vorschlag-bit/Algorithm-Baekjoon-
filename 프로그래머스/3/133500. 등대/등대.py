import sys
sys.setrecursionlimit(10**6)
def solution(n, lh):
    graph = [[] for _ in range(n+1)]
    for a,b in lh:
        graph[a].append(b)
        graph[b].append(a)
    dp = [[0,1] for _ in range(n+1)]
    def dfs(cur,parent):
        nonlocal graph,dp
        for child in graph[cur]:
            if child == parent: continue
            dfs(child,cur)
            dp[cur][0] += dp[child][1]
            dp[cur][1] += min(dp[child][0],dp[child][1])
    dfs(1,-1)
    return min(dp[1][0],dp[1][1])