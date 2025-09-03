from sys import stdin as input

n = int(input.readline())
arr = [list(map(int, input.readline().split())) for _ in range(n)]

# DP 테이블: dp[i][j][direction]
# direction: 0=가로, 1=세로, 2=대각선
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

# 초기값: (0,1) 위치에 가로 방향으로 1개
dp[0][1][0] = 1

def check(x, y):
    return 0 <= x < n and 0 <= y < n and arr[x][y] == 0

for i in range(n):
    for j in range(n):
        # 현재 위치가 벽이면 스킵
        if arr[i][j] == 1:
            continue
            
        # 가로 방향에서 올 수 있는 경우
        if dp[i][j][0] > 0:
            # 가로 → 가로
            if check(i, j + 1):
                dp[i][j + 1][0] += dp[i][j][0]
            
            # 가로 → 대각선 (3칸 모두 확인)
            if (check(i, j + 1) and check(i + 1, j) and check(i + 1, j + 1)):
                dp[i + 1][j + 1][2] += dp[i][j][0]
        
        # 세로 방향에서 올 수 있는 경우
        if dp[i][j][1] > 0:
            # 세로 → 세로
            if check(i + 1, j):
                dp[i + 1][j][1] += dp[i][j][1]
            
            # 세로 → 대각선
            if (check(i, j + 1) and check(i + 1, j) and check(i + 1, j + 1)):
                dp[i + 1][j + 1][2] += dp[i][j][1]
        
        # 대각선 방향에서 올 수 있는 경우
        if dp[i][j][2] > 0:
            # 대각선 → 가로
            if check(i, j + 1):
                dp[i][j + 1][0] += dp[i][j][2]
            
            # 대각선 → 세로
            if check(i + 1, j):
                dp[i + 1][j][1] += dp[i][j][2]
            
            # 대각선 → 대각선
            if (check(i, j + 1) and check(i + 1, j) and check(i + 1, j + 1)):
                dp[i + 1][j + 1][2] += dp[i][j][2]

# 최종 답: (n-1, n-1) 위치에 도달하는 모든 방법의 수
print(dp[n-1][n-1][0] + dp[n-1][n-1][1] + dp[n-1][n-1][2])