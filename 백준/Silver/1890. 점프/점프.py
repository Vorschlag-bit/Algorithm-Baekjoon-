from sys import setrecursionlimit, stdin
setrecursionlimit(10**6)
input = stdin
n = int(input.readline())
arr = [list(map(int,input.readline().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]
def dfs(x,y):
    if x == n-1 and y == n-1:
        return 1
    if dp[x][y] != -1: return dp[x][y]
    dp[x][y] = 0
    step = arr[x][y]
    for i in [(step,0),(0,step)]:
        nx,ny = x + i[0], y + i[1]
        if 0 <= nx < n and 0 <= ny < n:
            dp[x][y] += dfs(nx,ny)
    return dp[x][y]
print(dfs(0,0))