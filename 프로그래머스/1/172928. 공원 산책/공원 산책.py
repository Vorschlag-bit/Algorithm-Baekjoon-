from collections import deque
def solution(park, routes):
    dic = {"E":0,"S":1,"W":2,"N":3}
    # e,s,w,n
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    q = deque()
    n = len(park) # 행(세로) h
    m = len(park[0]) # 열(가로) w
    cx,cy = 0,0
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                cx,cy = i,j
    for cmd in routes:
        d,step = cmd.split()
        step = int(step)
        d = direction[dic[d]]
        nx,ny = cx,cy
        flag = True
        for i in range(step):
            a,b = nx+d[0],ny+d[1]
            if 0 <= a < n and 0 <= b < m and park[a][b] != 'X':
                nx,ny = a,b
            else:
                flag = False
                nx,ny = cx,cy
        if flag:
            cx,cy = nx,ny
    return [cx,cy]