def solution(info, n, m):
    ans = float('inf')
    l = len(info)
    visit = set()
    def dfs(idx,a_sum,b_sum):
        nonlocal ans,l,n,m
        if a_sum >= n: return
        if b_sum >= m: return
        if a_sum >= ans: return
        if idx == l:
            ans = min(ans,a_sum)
            return
        k = (idx,a_sum,b_sum)
        if k in visit:
            return
        visit.add(k)
        dfs(idx+1,a_sum+info[idx][0],b_sum)
        dfs(idx+1,a_sum,b_sum+info[idx][1])
    dfs(0,0,0)
    return ans if ans < n else -1