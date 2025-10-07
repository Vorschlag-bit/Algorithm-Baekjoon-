def solution(board, A, B):
    ans = 0
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    n = len(board)
    m = len(board[0])
    def check(x,y): return 0 <= x < n and 0 <= y < m

    def dfs(players,c_board,turn,total):
        # 현재 움직여야할 플레이어
        cx,cy = players[turn]
        # 상대 플레이어
        ex,ey = players[1-turn]
        # 현재 이동 가능한지 혹은 패배했는지 체크
        if c_board[cx][cy] == 0:
            # 이긴 사람, 총 움직임
            return (1-turn,total)
        # 상하좌우 중 갈 수 있는 곳으로 전부 다 이동
        flag = True
        results = []
        for d in directions:
            nx,ny = cx + d[0], cy + d[1]
            if check(nx,ny) and c_board[nx][ny] != 0:
                flag = False
                copy = [c[:] for c in c_board[:]]
                copy[cx][cy] = 0
                if turn == 0: r = dfs([(nx,ny),(ex,ey)],copy,1-turn,total+1)
                else: r = dfs([(ex,ey),(nx,ny)],copy,1-turn,total+1)
                results.append(r)
        # 움직이지 못하면 패배
        if flag:
            return (1-turn,total)
        win = [r for r in results if r[0] == turn]
        # 승리가 있다면 최소
        if win: best = min(win,key=lambda x: x[1])
        # 없다면 최대
        else: best = max(results,key=lambda x: x[1])
        return best
        
    result = []
    # A에 대해서 모든 이동 시뮬레이션
    for d in directions:
        nx,ny = A[0] + d[0], A[1] + d[1]
        if check(nx,ny) and board[nx][ny] == 1:
            copy = [b[:] for b in board[:]]
            copy[A[0]][A[1]] = 0
            # (w,turn) w -> 0 == A, 1 == B
            r = dfs([(nx,ny),(B[0],B[1])],copy,1,1)
            result.append(r)
    # 만약 아무도 이동 못하면 0 return
    if not result:
        return 0
    # A의 승리
    a_win = [r for r in result if r[0] == 0]
    if a_win:
        best = min(a_win,key=lambda x: x[1])
    else:
        best = max(result,key=lambda x: x[1])
    return best[1]