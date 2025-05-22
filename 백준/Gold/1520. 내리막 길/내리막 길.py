from sys import stdin as input
import sys
sys.setrecursionlimit(10**6)
n,m = map(int,input.readline().split())
arr = [list(map(int,input.readline().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
direction = [(0,1),(1,0),(-1,0),(0,-1)]
def dfs(x,y):
    if x == n - 1 and y == m - 1: return 1
    if dp[x][y] != -1: return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx,ny = x+direction[i][0], y+direction[i][1]
        if 0<=nx<n and 0<=ny<m and arr[x][y] > arr[nx][ny]:
            dp[x][y] += dfs(nx,ny)
    return dp[x][y]
print(dfs(0,0))