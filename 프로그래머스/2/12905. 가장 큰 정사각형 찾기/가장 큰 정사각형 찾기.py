def solution(board):
    ans = 0
    n = len(board)
    m = len(board[0])
    dp = [[0]*m for _ in range(n)]
    for i in range(n):
        dp[i][0] = board[i][0]
    for j in range(m):
        dp[0][j] = board[0][j]
    for i in range(1,n):
        for j in range(1,m):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    for i in range(n):
        for j in range(m):
            ans = max(ans,dp[i][j])

    return ans*ans