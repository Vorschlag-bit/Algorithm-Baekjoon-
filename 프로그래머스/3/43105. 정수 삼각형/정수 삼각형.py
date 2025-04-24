def solution(t):
    ans = 0
    n = len(t)
    if n == 1:
        return t[0][0]
    dp = [[0] * n for _ in range(n)]
    # 양쪽 끝부터 다 채워넣기
    dp[0][0] = t[0][0]
    for i in range(1,n):
        dp[i][0] = dp[i-1][0] + t[i][0]
        dp[i][i] = dp[i-1][i-1] + t[i][i]
    for i in range(2,n):
        for j in range(1,i):
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + t[i][j]
            ans = max(ans, dp[i][j])
    return ans