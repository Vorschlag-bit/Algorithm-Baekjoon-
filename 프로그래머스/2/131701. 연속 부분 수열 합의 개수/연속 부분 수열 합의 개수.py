def solution(elements):
    n = len(elements)
    elements += elements
    ans = set()
    dp = [[0]*(2*n) for _ in range(n+1)]
    for i in range(2*n):
        dp[1][i] = elements[i]
        ans.add(dp[1][i])
    for l in range(2,n+1):
        for i in range(2*n-l):
            dp[l][i] = dp[l-1][i] + dp[l-1][i+1] - dp[l-2][i+1]
            ans.add(dp[l][i])
    return len(ans)