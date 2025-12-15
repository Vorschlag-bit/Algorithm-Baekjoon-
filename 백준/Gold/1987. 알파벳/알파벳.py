from sys import stdin as input
import sys
sys.setrecursionlimit(10**5)
n,m = map(int, input.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(str,input.readline().rstrip())))

directions = [(0,1),(1,0),(0,-1),(-1,0)]
visit = [False] * 26

def check(a,b):
    return 0 <= a < n and 0 <= b < m

ans = 0
start = ord(arr[0][0]) - 65
visit[start] = True

def dfs(cx,cy,step,visit):
    global ans
    ans = max(ans, step)

    for d in directions:
        nx,ny = cx + d[0], cy + d[1]
        if not check(nx,ny): continue
        char = ord(arr[nx][ny]) - 65
        if visit[char]: continue
        visit[char] = True
        dfs(nx,ny,step+1,visit)
        visit[char] = False

dfs(0,0,1,visit)
print(ans)