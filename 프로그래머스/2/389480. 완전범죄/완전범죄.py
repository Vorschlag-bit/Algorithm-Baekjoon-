def solution(info, n, m):
    ans = float('inf')
    visit = set()
    def dfs(aSum,bSum,idx):
        nonlocal ans
        if aSum >= n:
            return
        if bSum >= m:
            return
        if aSum >= ans:
            return
        if idx == len(info):
            # 물건을 다 훔쳤을 때, 최소의 answer
            ans = min(ans, aSum)
            return
        if (aSum,bSum,idx) in visit:
            return
        visit.add((aSum,bSum,idx))
        dfs(aSum + info[idx][0],bSum,idx+1)
        dfs(aSum, bSum + info[idx][1],idx+1)
    dfs(0,0,0)
    return ans if ans < n else -1