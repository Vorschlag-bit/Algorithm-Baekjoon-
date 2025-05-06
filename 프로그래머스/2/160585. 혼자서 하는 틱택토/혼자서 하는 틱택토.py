from collections import Counter
def win(p,board):
    for i in range(3):
        if all(board[i][j] == p for j in range(3)): return True
        if all(board[j][i] == p for j in range(3)): return True
    if all(board[i][i] == p for i in range(3)):return True
    if all(board[i][2-i] == p for i in range(3)): return True
    return False
def solution(board):
    c = Counter(''.join(board))
    o = c.get('O',0)
    x = c.get('X',0)
    # if not (o == x or o == x + 1):
    #     return 0
    ow = win('O',board)
    xw = win('X',board)
    if not (o == x or o == x+1):
        return 0
    # 둘 다 이기면 0
    if ow and xw:
        return 0
    # o가 이겼는데 x가 o개 이상일 경우
    if ow and x+1 != o:
        return 0
    if xw and o != x:
        return 0
    return 1