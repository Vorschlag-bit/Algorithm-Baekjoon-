def solution(board, skill):
    ans = 0
    n = len(board)
    m = len(board[0])
    diff = [[0] * (m+1) for _ in range(n+1)]
    # 행 -> 열 순으로 반영
    for t,r1,c1,r2,c2,d in skill:
        # 공격
        if t == 1: d = -d
        diff[r1][c1] += d
        diff[r2+1][c2+1] += d
        diff[r1][c2+1] -= d
        diff[r2+1][c1] -= d
    for i in range(n):
        for j in range(m):
            diff[i][j+1] += diff[i][j]
    for j in range(m):
        for i in range(n):
            diff[i+1][j] += diff[i][j]
    for i in range(n):
        for j in range(m):
            board[i][j] += diff[i][j]
            if board[i][j] > 0: ans += 1
    return ans