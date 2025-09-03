from sys import stdin as input

n = int(input.readline())
arr = [list(map(int, input.readline().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

def check(x,y):
    global arr
    return 0 <= x < n and 0 <= y < n and arr[x][y] != 1

def cross(x,y):
    nx1,ny1 = x+1,y
    nx2,ny2 = x+1,y+1
    nx3,ny3 = x,y+1
    return check(nx1,ny1) and check(nx2,ny2) and check(nx3,ny3)

# (0,1) 가로 1개
dp[0][1][0] = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1: continue

        # 가로
        if dp[i][j][0] > 0:
            # 가로
            if check(i,j+1): dp[i][j+1][0] += dp[i][j][0]
            # 대각선
            if cross(i,j): dp[i+1][j+1][2] += dp[i][j][0]
        # 세로
        if dp[i][j][1] > 0:
            # 세로
            if check(i+1,j): dp[i+1][j][1] += dp[i][j][1]
            # 대각선
            if cross(i,j): dp[i+1][j+1][2] += dp[i][j][1]
        # 대각선
        if dp[i][j][2] > 0:
            # 가로
            if check(i,j+1): dp[i][j+1][0] += dp[i][j][2]
            # 세로
            if check(i+1,j): dp[i+1][j][1] += dp[i][j][2]
            # 대각선
            if cross(i,j): dp[i+1][j+1][2] += dp[i][j][2]
print(sum(dp[n-1][n-1][i] for i in range(3)))