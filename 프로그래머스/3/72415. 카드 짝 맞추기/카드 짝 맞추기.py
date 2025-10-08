from collections import deque,defaultdict

def check(x,y): return 0 <= x < 4 and 0 <= y < 4

def solution(board, r, c):
    ans = 0
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    pair = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                num = board[i][j]
                pair[num].append((i,j))
    
    pair_l = list(pair.values())
    
    def get_d(sx,sy,tx,ty,b):
        if sx == tx and sy == ty: return 0
        q = deque()
        visit = [[False] * 4 for _ in range(4)]
        visit[sx][sy] = True
        q.append((sx,sy,0))
        while q:
            cx,cy,dis = q.popleft()
            # 1칸 이동
            for d in directions:
                nx,ny = cx + d[0], cy + d[1]
                if check(nx,ny) and not visit[nx][ny]:
                    if tx == nx and ty == ny:
                        return dis + 1
                    visit[nx][ny] = True
                    q.append((nx,ny,dis+1))
            # 순간 이동
            for d in directions:
                nx,ny = cx,cy
                while True:
                    nx,ny = nx + d[0], ny + d[1]
                    # 1칸 전으로 이동
                    if not check(nx,ny):
                        nx,ny = nx - d[0], ny - d[1]
                        break
                    # 카드를 만나면 break
                    if b[nx][ny] > 0: break
                if not visit[nx][ny]:
                    if nx == tx and ny == ty:
                        return dis + 1
                    visit[nx][ny] = True
                    q.append((nx,ny,dis+1))
        return float('inf')
            
    def dfs(x,y,r,move,board):
        # 남은 카드 쌍이 없으면 move return
        if not r: return move
    
        min_d = float('inf')
        
        # 남은 카드쌍에서 하나 고르기
        for i in range(len(r)):
            # 카드 위치
            c1,c2 = r[i]
            
            # c1 -> c2(m1)
            d1 = get_d(x,y,c1[0],c1[1],board)
            d2 = get_d(c1[0],c1[1],c2[0],c2[1],board)
            # 이동 거리 + enter 2번
            m1 = d1 + d2 + 2
            # c2 -> c1(m2)
            d3 = get_d(x,y,c2[0],c2[1],board)
            d4 = get_d(c2[0],c2[1],c1[0],c1[1],board)
            m2 = d3 + d4 + 2
            
            for m,end_p in [(m1,c2),(m2,c1)]:
                # 복사 후 두 카드 뒤집기
                copy = [row[:] for row in board[:]]
                copy[c1[0]][c1[1]] = 0
                copy[c2[0]][c2[1]] = 0
                new_r = r[:i] + r[i+1:]
                
                result = dfs(end_p[0],end_p[1],new_r,m+move,copy)
                min_d = min(min_d, result)
        return min_d    
    # x,y,남은 거,총 움직임, 보드
    return dfs(r,c,pair_l,0,board)