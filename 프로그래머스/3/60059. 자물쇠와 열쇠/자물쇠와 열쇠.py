def solution(key, lock):
    n = len(lock)
    m = len(key)
    board = [[0]*(n+2*m-2) for _ in range(n+2*m-2)]
    for i in range(m-1,m+n-1):
        for j in range(m-1,m+n-1):
            board[i][j] += lock[i-m+1][j-m+1]
    b = len(board)
    def rotate(arr):
        return [[arr[m-1-j][i] for j in range(m)] for i in range(m)]
    def check(arr):
        for i in range(m-1,m+n-1):
            for j in range(m-1,m+n-1):
                if arr[i][j] != 1: return False
        return True
    rt_key = [key]
    for _ in range(3):
        rt_key.append(rotate(rt_key[-1]))
    for rk in rt_key:
        for i in range(m+n-1):
            for j in range(m+n-1):
                # i,j가 시작점
                copy = [board[a][:] for a in range(b)]
                for x in range(m):
                    for y in range(m):
                        copy[i+x][j+y] += rk[x][y]
                if check(copy): return True
    return False