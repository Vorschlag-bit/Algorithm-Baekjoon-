import sys
sys.setrecursionlimit(10000)
def solution(maze):
    ans = float('inf')
    directions = [(1,0),(0,1),(0,-1),(-1,0)]
    # 각 턴마다 반드시 모든 수레를 상하좌우 인접한 칸 중 한 칸으로 이동
    # check, 재방문 불가, 도착 시 이동 금지, 두 개 같은 칸 불가, 위치 스왑 불가
    n = len(maze)
    m = len(maze[0])
    rx,ry,bx,by = -1,-1,-1,-1
    rtx,rty,btx,bty = -1,-1,-1,-1
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                rx,ry = i,j
            elif maze[i][j] == 2:
                bx,by = i,j
            elif maze[i][j] == 3:
                rtx,rty = i,j
            elif maze[i][j] == 4:
                btx,bty = i,j
    # 5는 벽으로 모두 이동 불가
    r_visit = [[False] * m for _ in range(n)]
    r_visit[rx][ry] = True
    b_visit = [[False] * m for _ in range(n)]
    b_visit[bx][by] = True
    
    def check(x,y): return 0 <= x < n and 0 <= y < m

    # idx == 0 -> r, 1 -> b move
    def dfs(turn,rx,ry,bx,by,r_visit,b_visit):
        nonlocal rtx,rty,btx,bty,ans,maze
        if rx == rtx and ry == rty and bx == btx and by == bty:
            ans = min(ans,turn)
            return
        
        if turn >= ans: return
        
        # 동시에 move
        for d1 in directions:
            # 이미 도착했다면 pass
            if rx == rtx and ry == rty:
                nrx,nry = rx,ry
            else:
                nrx,nry = rx + d1[0], ry + d1[1]
            # 방문했거나 격자 벗어나거나 벽이면 금지
                if not check(nrx,nry) or r_visit[nrx][nry] or maze[nrx][nry] == 5: continue
    
            for d2 in directions:
                if bx == btx and by == bty:
                    nbx,nby = bx,by
                else:
                    nbx,nby = bx + d2[0], by + d2[1]
                # 방문했거나 격자 벗어나거나 벽이면 금지
                    if not check(nbx,nby) or b_visit[nbx][nby] or maze[nbx][nby] == 5: continue
                # 다른 수레와 스왑 금지
                if nrx == bx and nry == by and nbx == rx and nby == ry: continue
                # 같은 곳 이동 금지
                if nrx == nbx and nry == nby: continue
                # 이미 도착한 곳이 있다면 bt할 필요 없다
                if r_visit[nrx][nry] and not b_visit[nbx][nby]:
                    b_visit[nbx][nby] = True
                    dfs(turn+1,nrx,nry,nbx,nby,r_visit,b_visit)
                    b_visit[nbx][nby] = False
                elif not r_visit[nrx][nry] and b_visit[nbx][nby]:
                    r_visit[nrx][nry] = True
                    dfs(turn+1,nrx,nry,nbx,nby,r_visit,b_visit)
                    r_visit[nrx][nry] = False
                elif not r_visit[nrx][nry] and not b_visit[nbx][nby]:
                    r_visit[nrx][nry] = True
                    b_visit[nbx][nby] = True
                    dfs(turn+1,nrx,nry,nbx,nby,r_visit,b_visit)
                    r_visit[nrx][nry] = False
                    b_visit[nbx][nby] = False
                
    dfs(0,rx,ry,bx,by,r_visit,b_visit)
    return 0 if ans == float('inf') else ans