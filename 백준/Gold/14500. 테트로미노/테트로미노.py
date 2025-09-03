from sys import stdin as input
n,m = map(int,input.readline().split())
arr = [list(map(int,input.readline().split())) for _ in range(n)]
# i,j에서 4칸 이동했을 경우의 최댓값만 구하기
directions = [(0,1),(1,0),(-1,0),(0,-1)]
ans = 0
visit = [[False] * m for _ in range(n)]
def check(x,y):
    return 0 <= x < n and 0 <= y < m
# 'ㅗ' 모양은? -> 탐색한 척하고 다시 탐색
def dfs(x,y,s,cnt):
    global ans,arr,visit
    if cnt == 4:
        ans = max(ans,s)
        return
    
    for d in directions:
        nx,ny = x + d[0], y + d[1]
        if check(nx,ny) and not visit[nx][ny]:
            if cnt == 2:
                visit[nx][ny] = True
                # 다시 제자리에서 dfs
                dfs(x,y,s+arr[nx][ny],cnt+1)
                visit[nx][ny] = False
            visit[nx][ny] = True
            dfs(nx,ny,s+arr[nx][ny],cnt+1)
            visit[nx][ny] = False
for i in range(n):
    for j in range(m):
        visit[i][j] = True
        dfs(i,j,arr[i][j],1)
        visit[i][j] = False
print(ans)   