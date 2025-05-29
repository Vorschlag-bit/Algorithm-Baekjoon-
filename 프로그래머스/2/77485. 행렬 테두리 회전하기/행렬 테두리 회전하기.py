def solution(r, c, queries):
    ans = []
    board = [[0]*c for _ in range(r)]
    cnt = 1
    for i in range(r):
        for j in range(c):
            board[i][j] = cnt
            cnt += 1
    def rotate(x1, y1, x2, y2):
        v = float('inf')
        nonlocal board
        tmp = board[x1][y1]
        v = min(tmp,v)
        # top
        for i in range(y1+1,y2+1):
            board[x1][i],tmp = tmp,board[x1][i]
            v = min(tmp,v)
        # left
        for i in range(x1+1,x2+1):
            board[i][y2],tmp = tmp,board[i][y2]
            v = min(tmp,v)
        # bot
        for i in range(y2-1,y1-1,-1):
            board[x2][i],tmp = tmp,board[x2][i]
            v = min(tmp,v)
        # right
        for i in range(x2-1,x1-1,-1):
            board[i][y1],tmp = tmp,board[i][y1]
            v = min(tmp,v)
        return v
    for x1,y1,x2,y2 in queries:
        x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1
        ans.append(rotate(x1,y1,x2,y2))
    return ans