def solution(board, skill):
    n = len(board)
    m = len(board[0])
    answer = 0
    # 누적합 배열은 행,열 모두 크기가 +1이여야 한다.
    diff = [[0] * (m + 1) for _ in range(n + 1)]
    
    for typ,r1,c1,r2,c2,dg in skill:
        if typ == 1: dg = -dg
        
        diff[r1][c1] += dg
        diff[r2+1][c1] -= dg
        diff[r1][c2+1] -= dg
        diff[r2+1][c2+1] += dg
    
    # 행부터 누적합 시작(c1 + 1 ~ c2 + 1)
    for r in range(n):
        for c in range(1, m + 1):
            diff[r][c] += diff[r][c-1]
        
    # 열 누적합 시작(r1 + 1 ~ r2 + 1)
    for c in range(m):
        for r in range(1, n + 1):
            diff[r][c] += diff[r-1][c]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] + diff[i][j] > 0:
                answer += 1
    
    return answer